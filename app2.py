# request是一个请求对象
from flask import Flask, render_template, request, flash
import pymysql
import xlrd

app = Flask(__name__)

# 全局变量
data = []       # 获取数据库的训练结果
dic = {}        # 单条数据字典
upload_data = []  # 用户上传的批量文件
final_file_data = []      # 批量数据字典

'''
# 在页面出现的时候就初始化成字典
1）连接数据库取出数据
2）将数据转成字典形式
'''


@app.route('/')
def hello():
    # 从数据库读取数据
    db = pymysql.connect("localhost", "root", "yaopeijia", "fwwb", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT * FROM " + 'final_data'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            ls = []
            ls.append(row[0])
            ls.append(row[1])
            ls.append(row[2])
            ls.append(row[3])
            data.append(ls)
    except:
        print("Error: unable to fecth data")
    # 关闭数据库连接
    db.close()

    # 将数据转换成字典形式
    for row in data:
        # 标签不分开的话
        # dic[row[0]]=row[1]+" "+row[2]+" "+row[3]
        # 如果标签要分开的话
        dic[row[0]] = row[1:]

    print(dic["圣鸿 吸水茶巾 茶具茶道配件棉麻吸水加厚茶巾茶韵托茶布垫 灰色茶巾"])

    return render_template('test2.html')


@app.route('/search', methods=['GET', 'POST'])
def form():
    # 判断请求方式
    if request.method == 'POST':
        print('单条数据查询')
        # 获取请求参数
        search_text = request.form.get('search')
        print(search_text)
        final_data = dic[search_text]
        return render_template('test2.html', fianldata=final_data)


@app.route('/file', methods=['GET', 'POST'])
def file():
    # 判断请求方式
    if request.method == 'POST':
        print('上传文件进行多条数据查询')
        # 获取请求参数
        file = request.files['file']
        f = file.read()  # 文件内容
        file_data = xlrd.open_workbook(file_contents=f)
        table = file_data.sheets()[0]
        names = file_data.sheet_names()  # 返回book中所有工作表的名字
        status = file_data.sheet_loaded(names[0])  # 检查sheet1是否导入完毕
        print(status)
        nrows = table.nrows  # 获取该sheet中的有效行数
        ncols = table.ncols  # 获取该sheet中的有效列数
        print(nrows)
        print(ncols)

        for i in range(nrows):
            ls = []
            ls1 = []
            temp = table.col(0)[i].value
            ls.append(temp)
            temp1 = dic[temp]
            ls1.append(temp)
            ls1.append(temp1[0])
            ls1.append(temp1[1])
            ls1.append(temp1[2])
            upload_data.append(ls)
            final_file_data.append(ls1)
        print('upload_data', upload_data)
        print('final_file_data', final_file_data)
        count = 1
        for row in upload_data:
            if count==1:
                print('row', row)
                count=-1
        return render_template('test2.html', upload_data=upload_data)


@app.route('/file_find', methods=['GET', 'POST'])
def file_find():
    # 判断请求方式
    if request.method == 'POST':
        print('批量数据查询')
        return render_template('test2.html', final_file_data=final_file_data)

if __name__ == '__main__':
    app.run(debug=True)
