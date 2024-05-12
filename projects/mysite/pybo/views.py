from django.shortcuts import render

def home(request):
    # 메인 화면을 렌더링
    return render(request, 'home.html')

def imageSearch(request):
    # 이미지 검색
    return render(request, 'imageSearch.html')

def search(request):
    # 일반 검색
    return render(request, 'search.html')

def cart(request):
    # 장바구니
    return render(request, 'cart.html')

def profile(request):
    # 사용자 정보
    return render(request, 'profile.html')

def exchangeRate(request):
    # 환율 정보
    return render(request, 'exchangeRate.html')

def onlineMallInfo(request):
    # 판매처 정보 
    return render(request, 'onlineMallInfo.html')

def moveToSeller(request):
    # 판매처 이동 페이지
    return render(request, "moveToSeller.html")

def productDetail(request):
    # 세부 제품 정보
    return render(request, "productDetail.html")

def login(request):
    # 로그인
    return render(request, "login.html")