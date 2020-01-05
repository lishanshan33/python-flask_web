from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Grid,Scatter,Pie#引入图表制作所需要的一些函数
from pyecharts import options as opts #利用as将函数options制定为opts，方便下面的调用，此函数用于图表的各种配置
import pandas as pd #引入pandas
import numpy as np
from pyecharts.globals import ThemeType

df = pd.read_csv("API_SP.DYN.TFRT.IN_DS2_en_csv_v2_612877.csv",encoding = 'utf-8')
df5 = pd.read_csv("分省教育经费.csv",encoding = 'utf-8')
df5 = df5.dropna(axis=1, how='all')



def overlap_line_scatter(Country) -> Bar:
    Country_index = list(df["Country Name"]).index("{}".format(Country))
    df_c = df.iloc[Country_index].to_dict()
    df_k = list(df_c.keys())[4:]
    df_v = list(df_c.values())[4:]
    bar = (
        Bar(opts.InitOpts(width='1150px', height='550px'))  # opts.InitOpts(width = '810px',height = '500px')
            .add_xaxis(df_k)
            .add_yaxis("{}生育率/%".format(Country), df_v)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .add_yaxis)("商家B", Faker.values()
            .set_global_opts(title_opts=opts.TitleOpts(title="{}生育率历年趋势".format(Country), subtitle="",
                                                       subtitle_textstyle_opts=opts.TextStyleOpts(color="red",
                                                                                                  font_size=14,
                                                                                                  font_style="italic")),
                             legend_opts=opts.LegendOpts(pos_right="15%")
                             )

    )
    line = (
        Line()
            .add_xaxis(df_k)
            .add_yaxis("{}生育率/%".format(Country), df_v)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    )
    bar.overlap(line)
    return bar.render('templates/word_2.html')


def overlap_line_scatter3(city) -> Bar:
    city_index = list(df5["地区"]).index("{}".format(city))
    fxjy = list(df5.iloc[city_index].to_dict().values())[1:][::-1]
    fxjy = [int(fxjy[i]) for i in range(len(fxjy))]
    bar = (
        Bar(opts.InitOpts(width='1150px', height='550px',
                          theme=ThemeType.LIGHT))  # opts.InitOpts(width = '810px',height = '500px')
            .add_xaxis(list(df5.columns)[1:][::-1])
            .add_yaxis("教育经费支出", fxjy)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .add_yaxis)("商家B", Faker.values()
            .set_global_opts(title_opts=opts.TitleOpts(title="{}省教育经费情况".format(city), subtitle="",
                                                       subtitle_textstyle_opts=opts.TextStyleOpts(color="red",
                                                                                                  font_size=14,
                                                                                                  font_style="italic")),
                             legend_opts=opts.LegendOpts(pos_right="15%")
                             )

    )
    line = (
        Line()
            .add_xaxis(list(df5.columns)[1:][::-1])
            .add_yaxis("教育经费支出", fxjy)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    )
    bar.overlap(line)
    return bar.render('templates/word_5.html')
