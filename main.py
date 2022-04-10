import ffp
import ll1

formula_path = './formula.txt'
vt_path = './vt.txt'
predict_path = './predict.txt'
token_path = './token.txt'

# 生成ffp集
ffp.generateFFTSet(vt_path, formula_path)

# # 写predict集
# fp = open(predict_path,'w')
# for key in ffp.dic.keys():
#     for formula in ffp.dic[key].split(' | '):
#         for item in ffp.predictSet[key + ' = ' + formula]:
#             fp.write(item + ' ')
#         fp.write('\n')
# fp.close()

# ll1
data = ll1.ll1(token_path)

# 递归下降

# 可视化
from pyecharts import options as opts
from pyecharts.charts import Tree

c = (
    Tree()
        .add(
        "",
        [data],
        collapse_interval=2,
        orient="TB",
        label_opts=opts.LabelOpts(
            position="top",
            horizontal_align="right",
            vertical_align="middle",
            rotate=0,
        ),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="GrammarTree"))
        .render("GrammarTree.html")
)
