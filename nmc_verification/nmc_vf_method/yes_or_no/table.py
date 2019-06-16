

import sklearn
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import copy

def contingency_table(ob, fo,threshold_list = None,save_path = None, figsize=(9, 4), x_label=None, y_label=None, title='contingency table', fontsize=20,

                      fontproperties='KaiTi', col_labels=['yes', 'no', 'Total'], row_labels=['yes', 'no', 'Total']):
    # 扩展一下该函数的功能
    # 当threshold_list 为None时，ob和fo里的取值默认是只为0或1的，否则根据threshold_list 里的阈值判断ob和fo里的元素是0或1，进一步绘图
    #threshold_list 有多个取值时，每个表的title 需要显示等级的内容

    if threshold_list is None:
        cm = confusion_matrix(ob, fo)
        tn, fp, fn, tp = cm.ravel()
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[])
        table_vals = [[tn, fn, tn + fn], [fp, tp, fp + tp], [tn + fp, fn + tp, tn + fp + fn + tp]]

        # 表格左上角需标明行和列哪个是预报，哪个是实况
        my_table = plt.table(cellText=table_vals,
                             rowLabels=row_labels, colLabels=col_labels,
                             loc='center')


        my_table.set_fontsize(10)
        my_table.scale(0.7, 3.5)
        plt.text(0.05, 0.5, y_label, fontsize=fontsize, rotation=90)
        plt.text(0.5, 0.9, x_label, fontsize=fontsize)
        plt.title(title, fontproperties=fontproperties, fontsize=25)
        #plt.show()
    else:
        tn = len(threshold_list)
        # threshold_list 有1各阈值时，表titile不变

        # threshold_list 有多个取值时，每个表的title 需要显示等级的内容

        for i in range(len(threshold_list)):
            ob1 = copy.deepcopy(ob)
            fo1 = copy.deepcopy(fo)
            ob1[ob1>=threshold_list[i]] = 1
            ob1[ob1< threshold_list[i]] =0
            fo1[fo1>=threshold_list[i]] = 1
            fo1[fo1< threshold_list[i]] =0

            #绘制表格

    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path)

    #print("success")