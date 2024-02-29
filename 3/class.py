import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self._hash_password(password)
    
    def info(self):
        return f"{self.name}님의 회원정보"

    def _hash_password(self, password): #본인확인과정으로 이용해보기 (게시글 검색, 삭제)
        return hashlib.md5(password.encode()).hexdigest()

    def display(self):
        print("회원이름: {} 회원아이디: {}".format(self.name, self.username))

    def __repr__(self):
        return f"{self.name}({self.username})"

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__ (self):
        return f"{self.author} 작성 : {self.title}  {self.content}"

members = []
posts = []

while True:
    print("1. 회원 등록")
    print("2. 회원 정보 보기")
    print("3. 게시글 작성")
    print("4. 게시글 검색")
    print("0. 종료")

    choice = input("원하는 작업을 선택하세요 (숫자 입력): ")

    if choice == '1':
        member_commit = input("회원 등록을 하시겠습니까? 예(yes): ")
        if member_commit.lower() == 'yes':
            name = input("회원 이름을 작성해주세요: ")
            username = input("회원 ID를 작성해주세요: ")
            password = input("회원 비밀번호를 작성해주세요: ")
            new_member = Member(name, username, password)
            members.append(new_member)
            print("회원 등록이 완료되었습니다.")
        else:
            print("회원 등록이 취소되었습니다.")

    elif choice == '2':
        mem_info_commit = input("회원 정보를 보시겠습니까? 예(yes): ")
        if mem_info_commit.lower() == 'yes':
            print("모든 회원 정보: ")
            for member in members:
                print(repr(member))

    elif choice == '3':
        post_commit = input("게시글을 작성하시겠습니까? 예(yes): ")
        if post_commit.lower() == 'yes':
            for member in members:
                for i in range(3):
                    title = input("게시물 제목을 입력해주세요: ")
                    content = input("게시물 내용을 입력해주세요: ")
                    new_post = Post(title, content, member.username)
                    posts.append(new_post)
                    print("게시글 작성이 완료되었습니다.")

    elif choice == '4':
        search_commit = input("단어 또는 작성자를 검색하시겠습니까? 예(yes): ")
        if search_commit.lower() == 'yes':
            specific_word_or_author = input("검색할 단어 또는 아이디를 입력하세요 : ")
            print(f"게시글 제목 또는 '{specific_word_or_author}'가 작성자 이름이 포함된 게시물 :")
            for post in posts:
                if specific_word_or_author in post.content or specific_word_or_author == post.author.username:
                    print(repr(post))


    elif choice == '0':
        print("게시판이용을 중지합니다.")
        break

    else:
        print("올바른 글자를 입력해주세요.")
