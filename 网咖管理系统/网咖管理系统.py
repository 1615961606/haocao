import pymysql
print('网咖管理系统')



'''进入循环，判断，完成用户选择'''

while True:
	print('*'*50)
	print('欢迎来到操作系统')
	print("1:用户管理")
	print("2:会员管理")
	print("3:公告管理")
	print("4:贴吧管理")
	print("退出系统请按0")
	print('*'*50)

	q = int(input('请输入选择:'))
	if q == 1:
		
		
		while True:
			print('*'*50)

			print('您以进入用户管理系统')
			print("1:注册新用户")
			print("2:查看用户信息")
			print("3:修改用户信息")
			print("返回上一级请按0")
			print('*'*50)

			w = int(input("请输入选择"))
			if w == 1:
				
				
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					csl = conn.cursor()
 					sid = input('请输入编码:')   
 					name = input('请输入姓名:')
 					nl = input("请输入年龄:")
 					xb = input('请输入性别:')
 					zw = input('请输入职务:')
 					params = [sid,name,nl,xb,zw]
 					count=csl.execute('insert into 用户管理(id,姓名,年龄,性别,职务) values(%s,%s,%s,%s,%s)',params)
 					print(count)
 					print("出现1表示以成功，否则失败")
 					conn.commit()
 					csl.close()
 					#捕获异常 处理异常代码
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)




				e = input("返回上一级请按0")
				if e == 0:
					break
				
			if w == 2:
			
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					cur = conn.cursor()
 					sid = input('请输入您要查询的编码:')   
 					params = [sid]
 					cur.execute('select * from 用户管理 where id=(%s)',params)
 					
 					result = cur.fetchone()
 					print(result)
 					print("查询成功")
 					cur.close()
 					conn.close()
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)
				
				e = input("返回上一级请按0")
				if e == 0:
					break
			if w == 3:

				try:
					conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user='root',passwd='bc123',charset='utf8')
					cur = conn.cursor()
					name = input("请输入您要修改的姓名")
					nl = input("请输入您要修改的年龄")
					xb = input("请输入您要修改的性别")
					zw = input("请输入您要修改的职务")
					sid = input("请输入您要修改的编号")
					sname = [name,nl,xb,zw,sid]
					count = cur.execute('update 用户管理 set 姓名=%s,年龄=%s,性别=%s,职务=%s where id = %s',sname)
					print(count)
					print("出现1表示以成功，否则失败")
					conn.commit()
					cur.close()
					conn.close()
				except Exception as e:
					print("出现1表示以成功，否则失败")
					print(e)

				e = input("返回上一级请按0")
				if e == 0:
					break
				
			if w == 0:
				break
	if q == 2:
		
		while True:
			print('您已进入会员管理系统')
			print('1:注册新会员')
			print("2:会员管理信息")
			print("返回上一级请按0")
			w = int(input('请输入选择'))
			if w == 1:
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					csl = conn.cursor()
 					sid = input('请输入编码:')   
 					name = input('请输入姓名:')
 					nl = input("请输入年龄:")
 					xb = input('请输入性别:')
 					zw = input('请输入职务:')
 					params = [sid,name,nl,xb,zw]
 					count=csl.execute('insert into 会员管理(id,姓名,年龄,性别,职务) values(%s,%s,%s,%s,%s)',params)
 					print(count)
 					print("出现1表示以成功，否则失败")
 					conn.commit()
 					csl.close()
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)
			if w == 2:
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					cur = conn.cursor()
 					sid = input('请输入您要查询的编码:')   
 					params = [sid]
 					cur.execute('select * from 会员管理 where id=(%s)',params)
 					
 					result = cur.fetchone()
 					print(result)
 					print("查询成功")
 					cur.close()
 					conn.close()
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)
			if w == 0:
				break

	if q == 3:
		
		while True:
			print("您以进入公告管理")
			print("1:新增公告信息")
			print("2:查看公告信息")
			print("3:删除公告信息")
			print("返回主界面按0")
			w = int(input("请输入选择"))
			if w == 1:
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					csl = conn.cursor()
 					sid = input('请输入编码:')   
 					name = input('请输入公告内容:')
 					params = [sid,name]
 					count=csl.execute('insert into 公告管理(id,公告内容) values(%s,%s)',params)
 					print(count)
 					print("出现1表示以成功，否则失败")
 					conn.commit()
 					csl.close()
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)




				e = input("返回上一级请按0")
				if e == 0:
					break
			if w == 2:
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					cur = conn.cursor()
 					sid = input('请输入您要查询的编码:')   
 					params = [sid]
 					cur.execute('select * from 公告管理 where id=(%s)',params)
 					
 					result = cur.fetchone()
 					print(result)
 					print("查询成功")
 					cur.close()
 					conn.close()
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)
				
				e = input("返回上一级请按0")
				if e == 0:
					break
			if w == 3:
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					cur = conn.cursor()
 					sid = input('请输入您要删除的编码:')   
 					params = [sid]
 					count = cur.execute('delete from 公告管理 where id=%s',params)
 					
 					
 					print(count)
 					print("删除成功")
 					conn.commit()
 					cur.close()
 					conn.close()
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)
				
				e = input("返回上一级请按0")
				if e == 0:
					break
			if w == 0:
				break
	if q == 4:
		
		while True:
			print("您以进入贴吧管理")
			print("1:审核发言")
			print("2:删除发言")
			print("返回上一级请按0")
			w = int(input("请输入选择"))
			if w == 1:
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					cur = conn.cursor()
 					sid = input('请输入您要查询的编码:')   
 					params = [sid]
 					cur.execute('select * from 贴吧管理 where id=(%s)',params)
 					
 					result = cur.fetchone()
 					print(result)
 					print("查询成功")
 					cur.close()
 					conn.close()
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)
				
				e = input("返回上一级请按0")
				if e == 0:
					break
			if w== 2:
				try:
				 	conn=pymysql.connect(host='localhost',port=3306,db='网咖管理系统',user=    'root',passwd='bc123',charset='utf8')
 					cur = conn.cursor()
 					sid = input('请输入您要删除的编码:')   
 					params = [sid]
 					count = cur.execute('delete from 贴吧管理 where id=%s',params)
 					
 					
 					print(count)
 					print("删除成功")
 					conn.commit()
 					cur.close()
 					conn.close()
				except Exception as e:
 					print("出现1表示以成功，否则失败")
 					print(e)
				
				e = input("返回上一级请按0")
				if e == 0:
					break
			if w == 0:
				break
	if q == 0:
		break
