import jieba
import xlrd

file_name = u'登记内容_关门.xls'
zone_hy = ['美容美发', '美容', '美发', '管理', '服务', '早教', '培训', '健身', '游泳', '咨询']
zone_zz = ['有限公司', '俱乐部', '公司', '中心', '店', '馆']
zone_sz = ['江苏省', '江苏', '上海市', '上海', '苏州市', '苏州', '姑苏区', '沧浪区', '虎丘区', '高新技术开发区', '高新区',
           '新区', '开发区', '吴中区', '吴中', '相城区', '相城', '吴江区', '吴江', '常熟市', '常熟', '张家港市', '张家港',
           '昆山市', '昆山', '太仓市', '太仓', '工业园区', '园区']
zone_gs = ['观前街道', '平江街道', '苏锦街道', '娄门街道', '桃花坞街道', '城北街道', '双塔街道', '沧浪街道', '胥江街道',
           '吴门桥街道', '友新街道', '石路街道', '葑门街道', '金阊街道', '留园街道', '虎丘街道', '白洋湾街道', '白洋湾']
zone_xc = ['元和镇', '元和街道', '元和', '太平镇', '太平街道', '太平', '黄桥镇', '黄桥街道', '黄桥', '北桥镇',
           '北桥街道', '北桥', '望亭镇', '望亭', '黄埭镇', '黄埭', '渭塘镇', '渭塘', '阳澄湖镇']
zone_wz = ['苏苑街道', '香山街道', '城南街道', '胥口镇', '胥口', '郭巷镇', '郭巷', '东山镇', '东山', '木渎镇', '木渎',
           '光福镇', '光福', '甪直镇', '甪直', '渡村镇', '渡村', '藏书镇', '藏书', '横泾镇', '横泾', '浦庄镇', '浦庄',
           '开发区', '太湖旅游度假区']
zone_wj = ['黎里镇', '黎里', '盛泽镇', '盛泽', '七都镇', '七都', '桃源镇', '桃源', '震泽镇', '震泽', '平望镇', '平望',
           '同里镇', '同里', '松陵镇', '松陵街道', '松陵', '江陵镇', '江陵街道', '江陵', '横扇镇', '横扇街道', '横扇',
           '八坼镇', '八坼街道', '八坼']
zone_xq = ['狮山街道', '枫桥街道', '枫桥', '横塘街道', '横塘', '镇湖街道', '镇湖', '浒墅关经济开发区', '浒关经开区',
           '浒墅关镇', '浒墅关', '浒关', '通安镇', '通安', '东渚镇', '东渚', '苏州高新区出口加工区', '苏州高新出口加工区',
           '科技城', '苏州西部生态城', '保税物流中心']
zone_cs = ['虞山镇', '梅李镇', '梅李', '海虞镇', '海虞', '古里镇', '古里', '沙家浜镇', '支塘镇', '支塘', '董浜镇',
           '董浜', '尚湖镇', '辛庄镇', '辛庄', '碧溪新区', '碧溪', '东南街道', '东南开发区']
zone_ks = ['玉山镇', '巴城镇', '巴城', '花桥镇', '花桥', '周市镇', '周市', '千灯镇', '千灯', '陆家镇', '陆家', '张浦镇',
           '张浦', '周庄镇', '周庄', '锦溪镇', '锦溪', '淀山湖镇']
zone_zjg = ['杨舍镇', '杨舍', '塘桥镇', '塘桥', '金港镇', '金港', '锦丰镇', '锦丰', '乐余镇', '乐余', '凤凰镇', '凤凰',
            '南丰镇', '南丰', '大新镇', '大新']
zone_tc = ['城厢镇', '城厢', '浏河镇', '浏河', '浮桥镇', '浮桥', '沙溪镇', '沙溪', '璜泾镇', '璜泾', '双凤镇', '双凤',
           '港口开发区', '经济开发区', '科教新城']
zone_yq = ['娄葑街道', '娄葑', '斜塘街道', '斜塘', '唯亭街道', '唯亭', '胜浦街道', '胜浦', '湖西社区', '湖东社区',
           '东沙湖社区', '月亮湾社区']
# zone = zone_hy + zone_zz + zone_sz + zone_gs + zone_xc + zone_wz + zone_wj + zone_xq + zone_cs + zone_ks \
#        + zone_zjg + zone_tc + zone_yq
zone = zone_sz + zone_gs + zone_xc + zone_wz + zone_wj + zone_xq + zone_cs + zone_ks \
       + zone_zjg + zone_tc + zone_yq

def read_excel():
    wb = xlrd.open_workbook(filename=file_name)
    sheet1 = wb.sheet_by_name('查询结果')
    cols = sheet1.col_values(9)
    cols.pop(0)
    result_cols = []
    for row_txt in cols:
        for z in zone:
            row_txt = row_txt.replace(z, '')
        result_cols.append(row_txt[0:2])
    result_cols.sort()
    counts = {}
    for word in result_cols:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in items:
        word, count = i
        print("{0:<10}{1:>5}".format(word, count))

    # txt = ''.join(cols)
    # for z in zone:
    #     txt = txt.replace(z, '')
    # jlist = jieba.lcut(txt)
    # counts = {}
    # for word in jlist:
    #     if len(word) == 1:
    #         continue
    #     else:
    #         counts[word] = counts.get(word, 0) + 1
    # items = list(counts.items())
    # items.sort(key=lambda x:x[1], reverse=True)
    # for i in items:
    #     word, count = i
    #     print("{0:<10}{1:>5}".format(word, count))
    # jlist = jieba.lcut(txt)


if __name__ == '__main__':
    read_excel()