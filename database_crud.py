import copy
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv('database')
db_user = os.getenv('username')
db_pass = os.getenv('password')
db_host = os.getenv('host')
db_port = os.getenv('port')



with psycopg2.connect(database=db_name,
                      user=db_user,
                      password=db_pass,
                      host=db_host,
                      port=db_port) as conn:
    with conn.cursor() as cur:
        def create_table():
            create_table_query="""
            create table if not exists products(
            id               serial primary key,
            name             varchar(255) not null,
            image            varchar(255) not null unique ,
            is_liked         boolean not null default  false,
            updated_at       time default current_time);
            """
            cur.execute(create_table_query)
            conn.commit()
            print("table yaratildi ")
            return work_on_the_table()


        def insert_data():
            name=str(input("Enter your name: "))
            image=str(input("Enter your image: "))
            is_liked=bool(input("Enter your is_liked: "))
            insert_data_query="""
            insert into products(name, image, is_liked)
            values (%s, %s, %s);
            """
            cur.execute(insert_data_query, (name, image, is_liked))
            conn.commit()
            qadam=input("""
                yana malumat qoshasizmi
                   1. ha
                   2. yoq
                   >>>""")
            if qadam=="1":
                return insert_data()
            elif qadam=="2":
                return work_on_the_table()
            else:
                print("bunday qadam mavjud emas : EROR")


        def select_data():
            release=input("""
                 Enter your release:
                      1. barchasini chiqarish
                      2. qidrish
                      >>>>""")
            if release=='1':
                select_data_query="""
                select * from products order by id;
                """
                cur.execute(select_data_query)
                data=cur.fetchall()
                print(data)
                qadam = input("""
                                   1. orqaga
                                   >>>""")
                if qadam == "1":
                    return work_on_the_table()
                else:
                    print("bunday qadam mavjud emas : EROR")


            elif release=='2':
                select_data_query="""
                select * from products where name like '%a%'order by id;
                """
                cur.execute(select_data_query)
                data=cur.fetchall()
                print(data)
                qadam = input("""
                                                 1. orqaga
                                                 >>>""")
                if qadam == "1":
                    return work_on_the_table()
            else:
                print(f"{release} is not a valid choice ; ?")

        def update_table():
            is_liked=bool(input("Enter your is_liked: "))
            id=int(input("Enter your id: "))
            update_data_query="""
            update products set is_liked=%s where id=%s;
            """
            cur.execute(update_data_query, (is_liked, id))
            conn.commit()
            qadam = input("""
                            yana malumot ozgartirasizmi
                               1. ha
                               2. yoq
                               >>>""")
            if qadam == "1":
                return update_table()
            elif qadam == "2":
                return work_on_the_table()
            else:
                print("bunday qadam mavjud emas : EROR")


        def delete_table():
            delete_table_query="""
            delete from products where id=1;
            """
            cur.execute(delete_table_query, id)
            conn.commit()
            qadam = input("""
                            yana malumat ochirasimi
                               1. ha
                               2. yoq
                               >>>""")
            if qadam == "1":
                return delete_table()
            elif qadam == "2":
                return work_on_the_table()
            else:
                print("bunday qadam mavjud emas : EROR")


        def work_on_the_table():
            affairs=input("""
                 jadval ustida ishlash
                    1. create table
                    2. insert table
                    3. select table
                    4. update table
                    5. delete table
                       >>>>""")
            if affairs=='1':
                return create_table()
            elif affairs=='2':
                return insert_data()
            elif affairs=='3':
                return select_data()
            elif affairs=='4':
                return update_table()
            elif affairs=='5':
                return delete_table()
            else:
                print(f"{affairs} is not a valid option")


        if __name__ == '__main__':
            work_on_the_table()





















