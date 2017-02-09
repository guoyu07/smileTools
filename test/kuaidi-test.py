
from app.business.kuaidi import KuaiDiNiao
from app.handler import LoggerHandler

if __name__ == '__main__':

    # 加载日志
    LoggerHandler.__init()

    ShipperCode = input("请输入快递公司 \n")
    if ShipperCode == "" :
        exit("感谢使用")

    LogisticCode = input("请输入快递单号 \n")

    if LogisticCode == "" :
        exit("感谢使用")

    data = KuaiDiNiao.realtimeQuery(ShipperCode,LogisticCode)

    print(data)

    data1 = KuaiDiNiao.billnoQuery(LogisticCode)

    print(data1)