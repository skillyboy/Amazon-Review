
from django.urls import path
from . import views
from django.shortcuts import render
from application.models import *
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.utils.timezone import make_aware
import pandas as pd
import gzip
import json

# ===============================================
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Count, Q
from datetime import timedelta
from rest_framework import generics, filters,status
from .models import Review, Rating, Product, Category
from application.serializer import *
from django.db.models import Avg
# ===================================================
    
  


# Lists all categories
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Retrieves details of a category
class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Lists all products in a category
class CategoryProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)

# creates a new product in a specified category.
# POST /category/{category_id}/add
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        category_id = kwargs.get('category_id')
        try:
            category = Category.objects.get(id=category_id)
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(category=category)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
















# ====================================
# Lists all products
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieves details of a product
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# ==================================

# Lists all reviews of a product
class ProductReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Review.objects.filter(product=product_id)

#Retrieves the details of a single review
class ProductReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# ==================================



# DELETE /category/{category_id}/products
class CategoryProductsDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        category = kwargs.get('pk')
        try:
            products_to_delete = Product.objects.filter(category__id=category)
            products_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# add keyword to category
class CategoryEditView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'

    def update(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Category.DoesNotExist:
            return Response({"error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)

        keywords = request.data.get('keywords')
        if keywords:
            # Split the string into a list of keywords
            keyword_list = [kw.strip() for kw in keywords.split(",")]
            # Remove any empty strings
            keyword_list = [kw for kw in keyword_list if kw]
            # Join the list back into a comma-separated string
            new_keywords = ", ".join(keyword_list)
            category.keywords = new_keywords
            category.save()
            return Response(self.serializer_class(category).data)
        else:
            return Response({'keywords': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)


# delete all keywords in a category
class CategoryDeleteKeywordsView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'

    def update(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Category.DoesNotExist:
            return Response({"error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)

        category.keywords = None
        category.save()
        return Response(self.serializer_class(category).data)




# # delete a keywords in a category
# class CategoryDeleteOneKeywordView(generics.UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_url_kwarg = 'category_id'

#     def update(self, request, *args, **kwargs):
#         try:
#             category = self.get_object()
#         except Category.DoesNotExist:
#             return Response({"error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)

#         keyword = request.data.get('keyword')
#         if keyword:
#             keywords_list = [kw.strip() for kw in category.keywords.split(',') if kw.strip()]
#             if keyword in keywords_list:
#                 keywords_list.remove(keyword)
#                 category.keywords = ', '.join(keywords_list)
#                 category.save()
#                 return Response(self.serializer_class(category).data)
#             else:
#                 return Response({'keyword': 'This keyword is not in the list of keywords.'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'keyword': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)



# ==================================



class SetupCreateView(generics.CreateAPIView):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer

    def post(self, request, *args, **kwargs):
        serializer = SetupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KeywordCreateView(generics.CreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

    def post(self, request, *args, **kwargs):
        setup_id = kwargs.get('setup_id')
        try:
            setup = Setup.objects.get(id=setup_id)
            serializer = KeywordSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(setup=setup)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SetupListView(generics.ListAPIView):
    queryset = Setup.objects.all()
    serializer_class = SetupSerializer





# =====================

class ReviewAverageRating(APIView):
    def get(self, request):
        average_rating = Review.objects.aggregate(Avg('ratings'))['ratings__avg']
        return Response({'average_rating': average_rating})

class ReviewCount(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        count = self.get_queryset().count()
        return Response({"total_items": count})


    # List of Amazon Reviews

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()

        # Get the `date` query parameter from the URL
        date_param = self.request.query_params.get('date')

        if date_param:
            # Convert the date string to a datetime object
            date = timezone.datetime.strptime(date_param, '%Y-%m-%d').date()

            # Filter the queryset to only include reviews on the specified date
            queryset = queryset.filter(created_at__date=date)

        return queryset

    
    

class ProductRatingList(generics.ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Rating.objects.filter(product_id=product_id)


class ProductRatingDetail(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer





# # GET /product/{product_id}/reviews?filter=like4.7
# class ReviewFilterView(generics.ListAPIView):
#     serializer_class = ReviewSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['rating']

#     def get_queryset(self):
#         product_id = self.kwargs.get('product_id')
#         queryset = Review.objects.filter(product__id=product_id)
#         filter_keyword = self.request.query_params.get('filter')
#         if filter_keyword == 'like4.7':
#             queryset = queryset.filter(overall__gte=4.7)
#         return queryset


# class ProductRatingList(generics.ListAPIView):
#     serializer_class = RatingSerializer

#     def get_queryset(self):
#         product_id = self.kwargs['product_id']
#         return Rating.objects.filter(product_id=product_id)


# class ProductRatingDetail(generics.RetrieveAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer


# # GET /product/{product_id}/reviews/user
# class UserReviewView(generics.ListAPIView):
#     serializer_class = ReviewSerializer

#     def get_queryset(self):
#         product_id = self.kwargs.get('product_id')
#         queryset = Review.objects.filter(product__id=product_id, helpfulness='User Reviews (22)')
#         return queryset


# # GET /product/{product_id}/reviews/best_seller
# class BestSellerReviewView(generics.ListAPIView):
#     serializer_class = ReviewSerializer

#     def get_queryset(self):
#         product_id = self.kwargs.get('product_id')
#         queryset = Review.objects.filter(product__id=product_id, helpfulness='Best Seller (15)')
#         return queryset












# # Deletes all products in a category
# @api_view(['DELETE'])
# def delete_all_products_in_category(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     products = Product.objects.filter(category=category)
#     products.delete()
#     return Response({'success': True, 'message': f'All products in category {category_id} deleted'})


# # Adds keywords to a category
# @api_view(['PATCH'])
# def add_keywords_to_category(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     keywords = request.data.get('keywords', [])
#     category.keywords.add(*keywords)
#     category.save()
#     return Response({'success': True, 'message': f'Keywords added to category {category_id}'})

# # Adds a product to a category
# @api_view(['POST'])
# def add_product_to_category(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     product = Product.objects.create(
#         category=category,
#         asin=request.data.get('asin'),
#         title=request.data.get('title'),
#         brand=request.data.get('brand'),
#         price=request.data.get('price'),
#         description=request.data.get('description'),
#         imUrl=request.data.get('imUrl')
#     )
#     return Response({'success': True, 'message': f'Product {product.id} added to category {category_id}'})

# # Filters reviews based on parameters
# @api_view(['GET'])
# def filter_review(request):
#     min_rating = request.query_params.get('min_rating', None)
#     max_reviews = request.query_params.get('max_reviews', None)
#     max_critical_reviews = request.query_params.get('max_critical_reviews', None)
#     reviews = Review.objects.all()
#     if min_rating:
#         reviews = reviews.filter(overall__gte=float(min_rating))
#     if max_reviews:
#         reviews = reviews.annotate(num_reviews=Count('review_set')).filter(num_reviews__lte=int(max_reviews))
#     if max_critical_reviews:
#         reviews = reviews.annotate(num_crit_reviews=Count('review_set', filter=Q(review_set__overall__lte=3, review_set__review_time__gte=timezone.now()-timedelta(days=30)))).filter(num_crit_reviews__lte=int(max_critical_reviews))
#     serializer = ReviewSerializer(reviews, many=True)
#     return Response(serializer.data)


# # DELETE /category/{category_id}/products
# @api_view(['DELETE'])
# def delete_category_products(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)
#         products = Product.objects.filter(category=category)
#         products.delete()
#         return Response(status=204)
#     except Category.DoesNotExist:
#         return Response(status=404)


# # PUT /category/{category_id}/edit
# @api_view(['PUT'])
# def edit_category(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)
#         keywords = ['Moisturizer', 'Face oil', 'Face serum', 'Beauty cream', 'Cleanser', 
#                     'Face mask', 'Anti-aging cream', 'Night Cream', 'Sephora', 
#                     'Moisturizer', 'Face oil', 'Face serum', 'Beauty cream', 'Cleanser']
#         for keyword in keywords:
#             category.name += f', {keyword}'
#         category.save()
#         return Response(status=200)
#     except Category.DoesNotExist:
#         return Response(status=404)




# # POST /category/{category_id}/add
# @api_view(['POST'])
# def add_product(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)
#         product = Product(category=category)
#         # set product details from request data
#         product.save()
#         return Response(status=201)
#     except Category.DoesNotExist:
#         return Response(status=404)



# # GET /product/{product_id}/reviews?filter=like4.7
# @api_view(['GET'])
# def filter_reviews(request, product_id):
#     try:
#         filter_keyword = request.query_params.get('filter')
#         reviews = Review.objects.filter(product_id=product_id, review_text__icontains=filter_keyword)
#         serialized_reviews = [serialize_review(review) for review in reviews]
#         return Response(serialized_reviews, status=200)
#     except Product.DoesNotExist:
#         return Response(status=404)

# def serialize_review(review):
#     return {
#         'id': review.id,
#         'user_id': review.user_id,
#         'helpfulness': review.helpfulness,
#         'review_text': review.review_text,
#         'overall': review.overall,
#         'summary': review.summary,
#         'review_time': review.review_time
#     }


# # GET /product/{product_id}/reviews/user
# @api_view(['GET'])
# def get_user_reviews(request, product_id):
#     try:
#         reviews = Review.objects.filter(product_id=product_id, helpfulness__icontains='User Reviews')
#         serialized_reviews = [serialize_review(review) for review in reviews]
#         return Response(serialized_reviews, status=200)
#     except Product.DoesNotExist:
#         return Response(status=404)












# # ==========================================================


      

# def parse(path):
#     path = ('All_Beauty.json.gz')
#     g = gzip.open(path, 'rb')
#     for l in g:
#         yield json.loads(l)
        
# def indexer(request):
    
#     category = Category.objects.get(name='All Beauty')
#     for row in parse(path):
#         # Skip the row if any key is missing or empty
#         if any(not row[key] for key in row):
#             continue
        
#         # Skip the row if the review already exists in the database
#         review_text = row.get('reviewText')
#         if Review.objects.filter(reviewText=review_text).exists():
#             continue
#         if not review_text:
#             continue  # Skip to the next row
#         summary = row.get('summary', '')

#         # Convert the reviewTime string to a datetime object
#         review_time_str = row['reviewTime']
#         review_time = datetime.strptime(review_time_str, '%m %d, %Y')

#         # Check if the product with the given ASIN already exists in the database
#         product, created = Product.objects.get_or_create(asin=row['asin'], category=category)
#         if created:
#             product.save()  # Save the newly created product

#         # Check if the review with the given reviewText already exists in the database
#         review, created = Review.objects.get_or_create(
#         asin=row['asin'],
#         product=product,
#         ratings=row['overall'],
#         verified=row['verified'],
#         # reviewTime=row['reviewTime'],
#         reviewTime=review_time,
#         reviewerID=row['reviewerID'],
#         reviewerName=row['reviewerName'],
#         reviewText=review_text,
#         summary=summary,
#         category= category
#         )
#         if created:
#             review.save()  # Save the newly created review
#         print(row['asin'])

#     return render(request, 'index.html')

from datetime import datetime
from collections import defaultdict

def review_table(request):
    # Get the review data
    reviews = Review.objects.all()

    # Group the reviews by month and calculate the review count and average rating for each month
    month_data = defaultdict(lambda: {'count': 0, 'total_rating': 0})
    for review in reviews:
        if not review.reviewTime:
            continue
        review_date = datetime.strptime(review.reviewTime[:10], '%Y-%m-%d')
        month_str = review_date.strftime('%b, %Y')

        month_data[month_str]['count'] += 1
        month_data[month_str]['total_rating'] += review.ratings
    
    # Calculate the average rating for each month
    for month_str, data in month_data.items():
        if data['count'] > 0:
            data['average_rating'] = round(data['total_rating'] / data['count'], 1)
        else:
            data['average_rating'] = None
    
    # Sort the data by month in descending order
    sorted_month_data = sorted(month_data.items(), key=lambda x: datetime.strptime(x[0], '%b, %Y'), reverse=True)
    
    # Render the template with the review data
    return render(request, 'review_table.html', {'month_data': sorted_month_data})

























# # ratings
# # ratings = []
# # with gzip.open(path, 'rb') as f:
# #     for line in f:
# #         review = json.loads(line)
# #         ratings.append(review['overall'])

# # avg_rating = statistics.mean(ratings)
# # print(f"Average rating: {avg_rating:.2f}")



# def index(request):
#     content = "Hello, world!"
#     categories = [
#     'Amazon Fashion',
#     'All Beauty',
#     'Appliances',
#     'Arts, Crafts and Sewing',
#     'Automotive',
#     'Books',
#     'CDs and Vinyl',
#     'Cell Phones and Accessories',
#     'Clothing, Shoes and Jewelry',
#     'Digital Music',
#     'Electronics',
#     'Gift Cards',
#     'Grocery and Gourmet Food',
#     'Home and Kitchen',
#     'Industrial and Scientific',
#     'Kindle Store',
#     'Luxury Beauty',
#     'Magazine Subscriptions',
#     'Movies and TV',
#     'Musical Instruments',
#     'Office Products',
#     'Patio, Lawn and Garden',
#     'Pet Supplies',
#     'Prime Pantry',
#     'Software',
#     'Sports and Outdoors',
#     'Tools and Home Improvement',
#     'Toys and Games',
#     'Video Games',
# ]
#     if categories:
#         for category_name in categories:
#             Category.objects.create(name=category_name)
#         return HttpResponse(content)
#     else:
#         return HttpResponse()
#     return render(request, 'index.html')

    # def getDF(path):
    #     i = 0
    #     df = {}
    #     for d in parse(path):
    #         df[i] = d
    #         i += 1
    #     return pd.DataFrame.from_dict(df, orient='index')

    # # Call getDF function and store result in a variable
    # df = getDF(path)