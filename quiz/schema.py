import graphene
# this line below is work like serializer in REST
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Category, Question, Quiz, Answer
# from books.models import Books


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','name')

class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'category', 'quiz')


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz')


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question', 'answer_text')


class Query(graphene.ObjectType):
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        # here i have foreignkey so i can call best on that and get all the answer
        # by just one question
        return Answer.objects.filter(question=id)

    # quiz = graphene.String()
    # def resolve_quiz(root, info):
    #     return f'This is the first question'


    # all_quizzes = graphene.Field(QuizType, id=graphene.Int())

    # def resolve_all_quizzes(root, info, id):
    #     return Quiz.objects.get(pk=id)


    # all_questions = graphene.Field(QuestionType, id=graphene.Int())
    # all_answers = graphene.List(AnswerType, id=graphene.Int())


    # def resolve_all_questions(root, info, id):
    #     return Question.objects.get(pk=id)

    # def resolve_all_answers(root, info, id):
    #     return Answer.objects.filter(pk=id)

    # all_quizzes = DjangoListField(QuizType)
    # all_questions = DjangoListField(QuestionType)

    # def resolve_all_quizzes(root, info):
    #     return Quiz.objects.all()

    # def resolve_all_questions(root, info):
    #     return Question.objects.all()


    # this two line is also the same thing return
    # all_quizzes = DjangoListField(QuizType)
    # all_quizzes = graphene.List(QuizType)
    # all_questions = graphene.List(QuestionType)
    # all_answers = graphene.List(AnswerType)

    # def resolve_all_quizzes(root, info):
    #     return Quiz.objects.all()

    # def resolve_all_questions(root, info):
    #     return Question.objects.all()

    # def resolve_all_answers(root, info):
    #     return Answer.objects.all()



    # This two line bellow are the same, it means that work same way
    # all_quizzes = DjangoListField(QuizType)
    # all_quizzes = graphene.List(QuizType)
    # def resolve_all_quizzes(root, info):
    #     # to return specific id's or field
    #     return Quiz.objects.filter(id=2)


# class BooksType(DjangoObjectType):
#     class Meta:
#         model = Books
#         fields = ("id", "title", "excerpt")

# class Query(graphene.ObjectType):

#     all_books = graphene.List(BooksType)

#     def resolve_all_books(root, info):
#         return Books.objects.all()
#         # return Books.objects.filter(title="django books")

# schema = graphene.Schema(query=Query)



# class CategoryMutation(graphene.Mutation):
#     # in this class i can define method to save data
#     class Arguments:
#         name = graphene.String(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)


class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        # if you run for deleting you you need just 'id' so comment the line bellow
        # name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    # def mutate(cls, root, info, name, id):
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        # you can update or delete form here
        # category.name = name
        # category.save()
        # for deleting you don't need the name all you need to do is pass the 'id'
        category.delete()
        # for deleting you don't need the line bellow so i will commented
        # return CategoryMutation(category=category)
        return


class Mutation(graphene.ObjectType):
    # here we can add or update category
    # the mutations is work like post in REST
    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)