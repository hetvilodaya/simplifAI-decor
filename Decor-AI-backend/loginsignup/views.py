from django.shortcuts import render

# Create your views here.
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from collections import Counter
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .serializers import ProcessPDFSerializer
import replicate
import os
import base64
import logging
from PIL import Image
import io
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import spacy
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse

logger = logging.getLogger(__name__)

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
        os.environ["REPLICATE_API_TOKEN"] = "API_KEY"
        model = replicate.models.get('rossjillian/controlnet')
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

class ProcessPDFView(APIView):

    @csrf_exempt
    def get_pdf_text(self, pdf_filename):
        try:
            pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
            if not os.path.exists(pdf_path):
                logger.error(f"PDF file not found at: {pdf_path}")
                raise FileNotFoundError(f"PDF file not found at: {pdf_path}")
            
            text = ""
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    text += page.extract_text() if page.extract_text() else ''
            return text
        except Exception as e:
            logger.exception("Failed to process PDF.")
            raise e
    
    @csrf_exempt
    def get_text_chunks(self, text):
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        return chunks

    @csrf_exempt
    def get_vectorstore(self, text_chunks):
        embeddings = OpenAIEmbeddings()
        #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
        return vectorstore

    @csrf_exempt
    def get_conversation_chain(vectorstore):
        llm = ChatOpenAI()
        #llm = HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature":0.5, "max_length":512})
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        return conversation_chain
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        load_dotenv()
        try:
            data = json.loads(request.body.decode('ascii'))
            logger.info(f"Received data: {data}")
            serializer = ProcessPDFSerializer(data=data)

            if serializer.is_valid():
                pdf_filename = serializer.validated_data['pdf_file']
                user_question = serializer.validated_data['question']

                pdf_text = self.get_pdf_text(pdf_filename)
                text_chunks = self.get_text_chunks(pdf_text)
                vectorstore = self.get_vectorstore(text_chunks)
                conversation_chain = self.get_conversation_chain(vectorstore)

                if user_question:
                    response = conversation_chain({'question': user_question})
                    chat_history = response['chat_history']
                    response_content = [
                        {"content": message['content'], "sender": "user" if i % 2 == 0 else "bot"}
                        for i, message in enumerate(chat_history)
                    ]

                    # Return the AI response as JSON
                    return JsonResponse({"messages": response_content})
                else:
                    return JsonResponse({"error": "Please provide a question."}, status=400)
            else:
                logger.error(f"Invalid data: {serializer.errors}")
                return JsonResponse({"error": "Invalid data provided."}, status=400)
        except Exception as e:
            logger.exception("Error in processing request.")
            return JsonResponse({"error": str(e)}, status=500)
