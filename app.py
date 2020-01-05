from flask import Flask,render_template,url_for,request
from new_pyecharts import *
app = Flask(__name__)




@app.route('/')
def index():
    page_title = '交互式可视化数据故事'
    page_description = '这是python与交互式可视化自我策展成果主页'
    return render_template('default.html',title=page_title,
                            description=page_description,
                           content =render_template('index.html'))


#数据故事页面
@app.route('/jiaohu/')
def jiaohu():
    the_select_region = list(df["Country Name"])
    the_select_region_1 = df5.地区.tolist()
    # custommize your page title / description here
    page_title       = '交互式可视化数据故事'
    page_description = '这是python与交互式可视化自我策展成果'
    with open("templates/word_2.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    with open("templates/word_5.html", encoding="utf8", mode="r") as f1:
        word_5 = "".join(f1.readlines())
    return render_template('default.html',
                            title=page_title,
                            description=page_description,
                            content=render_template( 'jiaohu.html',word_1=render_template('word_1.html'),
                                                     word_2=plot_all,the_select_region = the_select_region,
                                                     the_select_region_1=the_select_region_1,
                                                     word_3=render_template('word_3.html'),
                                                     word_4=render_template('word_4.html'),
                                                     word_5=word_5,
                                                     word_6=render_template('word_6.html'))
                           )

#post请求功能页面跳转
@app.route('/jiaohu/1',methods=['POST'])
def jiaohu1():
    the_select_region = list(df["Country Name"])
    the_select_region_1 = list(df5["地区"])
    page_title = '交互式可视化数据故事'
    page_description = '这是python与交互式可视化自我策展成果'
    print(list(request.values.to_dict().keys())[0])
    if list(request.values.to_dict().keys())[0] == "the_region_selected":
        the_region = request.form["the_region_selected"]
        overlap_line_scatter(the_region)
        table_1 = pd.DataFrame(df.iloc[list(df["Country Name"]).index("{}".format(the_region))]).T.to_html()
        with open("templates/word_2.html", encoding="utf8", mode="r") as f:
            plot_all = "".join(f.readlines())
        return render_template('default.html',
                               title=page_title,
                               description=page_description,
                               content=render_template('jiaohu_1.html',
                                                       word_2=plot_all,
                                                       table_1=table_1,
                                                       the_select_region=the_select_region,
                                                       ))
    else:
        the_region_1 = request.form["the_region_selected_1"]
        overlap_line_scatter3(the_region_1)
        table_2 = pd.DataFrame(df5.iloc[list(df5["地区"]).index("{}".format(the_region_1))]).T.to_html()
        with open("templates/word_5.html", encoding="utf8", mode="r") as f1:
            plot_all_1 = "".join(f1.readlines())
        return render_template('default.html',
                               title=page_title,
                               description=page_description,
                               content=render_template('jiaohu_2.html',
                                                        word_5=plot_all_1,
                                                       table_2 = table_2,
                                                       the_select_region_1=the_select_region_1))


@app.route('/jiaohu_1')


#功能页面一
def jiaohu_1():
    table_1 = df.to_html()
    the_select_region = list(df["Country Name"])
    page_title = '交互式可视化数据故事'
    page_description = '这是python与交互式可视化自我策展成果'
    with open("templates/word_2.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    return render_template('default.html',
                               title=page_title,
                               description=page_description,
                               content=render_template('jiaohu_1.html',
                                                       word_2=plot_all,
                                                       table_1=table_1,
                                                       the_select_region=the_select_region,)
                               )


#功能页面二
@app.route('/jiaohu_2')
def jiaohu_2():
    table_2 = df5.to_html()
    page_title = '交互式可视化数据故事'
    page_description = '这是python与交互式可视化自我策展成果'
    the_select_region_1 = list(df5["地区"])
    with open("templates/word_5.html", encoding="utf8", mode="r") as f1:
        plot_all_1 = "".join(f1.readlines())
    return render_template('default.html',
                           title=page_title,
                           description=page_description,
                           content=render_template('jiaohu_2.html',
                                                   table_2=table_2,
                                                   the_select_region_1=the_select_region_1,
                                                   word_5=plot_all_1,
                                                   ),
                           )





if __name__ == '__main__':
    app.run()
