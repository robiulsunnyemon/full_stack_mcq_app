

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from tutor.views import QuestionViewSet,ChoiceViewSet,QuestionAnswerViewSet,CategoryquestionViewSet,student_leaderboard,CategoryBlogViewSet,UserDetailsViewSet,BlogViewSet,blogs_by_category,questions_by_category,choice_by_question_id,RegisterView,LoginView,BulkQuestionCreateView,BulkOptionsCreateView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('questions', QuestionViewSet)
router.register('options', ChoiceViewSet)
router.register('question_answers', QuestionAnswerViewSet)
router.register('question_categories', CategoryquestionViewSet)
router.register('blog_catagories',CategoryBlogViewSet)
router.register('user_details',UserDetailsViewSet)
router.register('blogs',BlogViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/student_leaderboard/', student_leaderboard, name='student_leaderboard'),
    path('api/questions/category/<int:category_id>/', questions_by_category, name='questions_by_category'),
    path('api/blog/category/<int:category_id>/', blogs_by_category, name='blogs_by_category'),
    path('api/choices/question/<int:question_id>/', choice_by_question_id, name='choice_by_question_id'),
    path('api/auth/signup/', RegisterView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('bulk-create-questions/', BulkQuestionCreateView.as_view(), name='bulk-create-questions'),
    path('bulk-options-questions/', BulkOptionsCreateView.as_view(), name='bulk-options-questions'),

]



# ইমেজ সেভ করার জন্য
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)