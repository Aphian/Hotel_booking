# Hotel_booking
---
## Summary
- 간단한 호텔예약 중계 사이트(Django MTV 활용)
- 사이트가 가지는 DB 로그인(유효성 검사를 위한 ModelForm)
- 소셜 로그인(Google, Naver, KaKao)
- 호텔 정보 Crawling
- 결제기능(추가하고 싶은 기능)
---
## Schedule
```
7.3. ~ 7.7. 
- 프로젝트 기초 설정(.gitgnore, README.md)
- User Model
- DB(sqllite)에 저장되는 login/join/logout 기능
- Home, navbar 생성
- Social Login(Google, Naver) allauth 패키지 활용
- Hotel_정보 모델링 / CRUD 기능 / 세분화 기능(보여주는 화면)
- Hotel_상품 리뷰 모델링 / CRUD 기능
- 공지사항 모델링 / CRUD 기능
- Book 모델링 / CRUD / 관계성 다시 파악
- Profile 목록(예약 내역 / 등록 목록)
- User 그룹화
7.10. ~ 7.14.
- login Form HTML
- Book DB 상태별 HTML 표시
- Social login 그룹화
- Template 분리
- Hotel_detail 세분화 기능
- Image 업로드 기능
- Template CSS 처리
7.18.
- Profile password 변경
- Template CSS 처리
7.19.
- 프로젝트 종료 / 발표
```
## Review and Development
- 개체들 간의 관계 모델링에 중요성을 다시 한번 느낌
- `erd`를 통해서 모델링을 해도 생각지도 못한 관계가 발생할 수 있음
- 상품이용날짜에 관한 검색 기능
- DB에 저장되어 있는 부분 뿐만 아니라 크롤링으로 데이터를 수집하여 사용해봐야할 듯
- 초기에 목표로한 Social Login 중 Kakao API를 사용하지 못함 -> 추가
- 부분 부분 찾을 경우가 많았는데 가독성이 낮았음 -> HTML 이나 views 부분에 해당하는 코드 주석 필요함