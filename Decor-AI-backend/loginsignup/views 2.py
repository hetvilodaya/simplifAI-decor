from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
import replicate
import os
import base64
from PIL import Image
import io
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class Newssource(APIView):
    def post(self, request):
        os.environ["REPLICATE_API_TOKEN"] = "r8_VHjBVBjw2jDcDobmBWabZxwcdozfPy73gTc9c"
        model = replicate.models.get('rossjillian/controlnet')
        # prompt = request.data['prompt']
        # print(prompt)
        # image = request.data['image']
        # print(image)
        data = json.loads(request.body)
        prompt = data['prompt']
        print("data", data['image'])
        data['image'] = data['image'].replace('data:image/jpeg;base64,', '')
        img = Image.open(io.BytesIO(
            base64.decodebytes(bytes(data['image'], "utf-8"))))
        #Image.save(img, "image.jpg")
        img.save("image.jpg")
        print(img)
        tol = model.predict(image=open('./image.jpg', "rb"),
                            prompt=prompt, structure="scribble", steps=20)
        print(tol)
        data = {'image': tol}
        return Response(data)


class pricecalculation(APIView):
    def post(self, request):
        # type_of_project = request.POST.get('type_of_project')
        # select_space = request.POST.get('select_space')
        # bhk = request.POST.get('bhk')
        carpet_area = request.POST.get('carpet_area')
        if 500 <= int(carpet_area) < 700:
            data = [{'title': 'Royale Shyne Luxury Emulsion', 'desc': 'Luxury has many forms, and one of them is the Royale Shyne Luxury Emulsion. A high sheen, washable wall paint with stain-resistant finish ensures walls look new for a long time. The paint’s high gloss and even smoother finish would make you want to stare at it all day. It’s the only paint emulsion in India equipped with Teflon surface protector that makes it highly durable.',
                     'ltr': '26 - 30 in litres', 'price': '₹23074 - 26370'}, {'title': 'Royale MATT', 'desc': 'Bumpless walls for a smooth look and luxurious feel, Royale Matt Luxury Emulsion gives the perfect matt finish to your walls. It’s the only', 'ltr': '26- 30', 'price': '23336 - 26670'},
                    {'title': 'Royale Luxury emulsion', 'desc': 'Luxury is just a brushstroke away with Royale Luxury Emulsion. It’s the only paint emulsion in India equipped with Teflon surface protector',
                     'ltr': '26-30', 'price': '21263 - 24300'}]
            return Response(data)
        if 700 <= int(carpet_area) < 1000:
            data = [{'title': 'Royale Shyne Luxury Emulsion', 'desc': 'Luxury has many forms, and one of them is the Royale Shyne Luxury Emulsion. A high sheen, washable wall paint with stain-resistant finish ensures walls look new for a long time. The paint’s high gloss and even smoother finish would make you want to stare at it all day. It’s the only paint emulsion in India equipped with Teflon surface protector that makes it highly durable.',
                     'ltr': '35-40 in litres', 'price': '₹30765 - 35160'}, {'title': 'Royale MATT', 'desc': 'Bumpless walls for a smooth look and luxurious feel, Royale Matt Luxury Emulsion gives the perfect matt finish to your walls. It’s the only', 'ltr': '35 - 40', 'price': '31115 - 35560'},
                    {'title': 'Royale Luxury emulsion', 'desc': 'Luxury is just a brushstroke away with Royale Luxury Emulsion. It’s the only paint emulsion in India equipped with Teflon surface protector',
                     'ltr': '23 - 28', 'price': '20067 - 24080'}]
            return Response(data)
        if 1000 <= int(carpet_area):
            data = [{'title': 'Royale Shyne Luxury Emulsion', 'desc': 'Luxury has many forms, and one of them is the Royale Shyne Luxury Emulsion. A high sheen, washable wall paint with stain-resistant finish ensures walls look new for a long time. The paint’s high gloss and even smoother finish would make you want to stare at it all day. It’s the only paint emulsion in India equipped with Teflon surface protector that makes it highly durable.',
                     'ltr': '48-55 in litres', 'price': '₹42302 - 48345'}, {'title': 'Royale MATT', 'desc': 'Bumpless walls for a smooth look and luxurious feel, Royale Matt Luxury Emulsion gives the perfect matt finish to your walls. It’s the only', 'ltr': '48 - 55', 'price': '42783 - 488895'},
                    {'title': 'Royale Luxury emulsion', 'desc': 'Luxury is just a brushstroke away with Royale Luxury Emulsion. It’s the only paint emulsion in India equipped with Teflon surface protector',
                     'ltr': '32-39', 'price': '27592 - 33110'}]
            return Response(data)

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os
import spacy
from collections import Counter

# Helper functions from your script
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def process_pdf_documents(text):
    text_chunks = get_text_chunks(text)
    vectorstore = get_vectorstore(text_chunks)
    conversation_chain = get_conversation_chain(vectorstore)
    return conversation_chain

# Django view
@csrf_exempt
def process_pdf_view(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('pdf_file')
        if not pdf_file:
            return HttpResponse("No PDF file uploaded.", status=400)
        
        file_path = default_storage.save(pdf_file.name, ContentFile(pdf_file.read()))
        pdf_docs = [default_storage.path(file_path)]
        
        pdf_text = get_pdf_text(pdf_docs)
        conversation_chain = process_pdf_documents(pdf_text)
        
        user_question = request.POST.get('question', '')
        if user_question:
            response = conversation_chain({'question': user_question})
            chat_history = response['chat_history']
            response_content = "<br>".join([f"User: {message['content']}" if i % 2 == 0 else f"Bot: {message['content']}" for i, message in enumerate(chat_history)])
            return HttpResponse(response_content, content_type="text/html")
        else:
            return HttpResponse("Please provide a question.", status=400)
    else:
        return HttpResponse('<form method="post" enctype="multipart/form-data">'
                            'PDF File: <input type="file" name="pdf_file"><br>'
                            'Question: <input type="text" name="question"><br>'
                            '<input type="submit" value="Submit">'
                            '</form>', content_type="text/html")

