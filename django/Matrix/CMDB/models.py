from django.db import models


# Asset
class Asset(models.Model):
    fixeCapitaldNumber = models.CharField(max_length=128,verbose_name="固资编号",unique=True)
    sn = models.CharField(max_length=128,verbose_name="SN序列号",unique=True)
    deviceName = models.CharField(max_length=128,verbose_name="设备名称",unique=True)
    manufacturerName = models.ForeignKey("manufacturer")
    deviceType = models.CharField(max_length=64,verbose_name="设备型号")
    purchaseDate = models.DateField(blank=True,null=True)
    expiredDate = models.DateField(blank=True,null=True)
    groundingDate = models.DateField(blank=True,null=True)
    enableDate = models.DateField(blank=True,null=True)
    departmentName = models.ForeignKey("department")
    ownerName = models.ForeignKey("owner")
    businessName = models.ManyToOneRel("business",blank=True)
    areaName = models.ForeignKey("area")
    networkAreaName = models.ForeignKey("networkArea")
    # idcName = models.ForeignKey("IDC")
    rackName = models.ForeignKey("rack")
    # idcManagementUnitName = models.ForeignKey("IDCManagementUnit")
    statusChoices = (
        (0,'运营中'),
        (1,'上架中'),
        (2,'故障'),
        (3,'备用'),
        (4,'过保'),
        (5,'报废'),
        (6,'失联')
    )
    statusName = models.SmallIntegerField(choices=statusChoices)








# Server
class Server(models.Model):
    asset = models.OneToOneField('Asset')
    osName = models.ForeignKey('os')
    oobIP = models.GenericIPAddressField(blank=True,null=True)
    hostIP = models.GenericIPAddressField(blank=True,null=True)
    wanIP = models.GenericIPAddressField(blank=True,null=True)
    deviceChoices = (
        (0,"虚拟机"),
        (1,"物理机")
    )
    deviceType = models.SmallIntegerField(choices=deviceChoices)

class os(models.Model):
    name = models.CharField(max_length=128,verbose_name="OS名称")
    versionChoices = (
        (0,'测试用'),
        (1,'线上用'),
        (2,'Bug存量'),
        (3,'维护中'),
        (4,'弃用')
    )
    version = models.SmallIntegerField(choices=versionChoices)

class ram(models.Model):
    asset = models.ForeignKey("Asset")
    manufacturer = models.ForeignKey("manufacturer")
    model = models.CharField(max_length=64)
    size = models.PositiveIntegerField("容量(GB)")
    ramType = models.CharField(max_length=64,verbose_name="RAM型号")
    slot = models.CharField(max_length=32,verbose_name="插槽")
    sn = models.CharField(max_length=128,unique=True)
    statusChoices = (
        (0, '使用中'),
        (1, '出库'),
        (2, '故障'),
        (3, '备用'),
        (4, '过保'),
        (5, '报废'),
        (6, '失联')
    )
    statusName = models.SmallIntegerField(choices=statusChoices)
    class Meta:
        unique_together = ("asset","slot")

class cpu(models.Model):
    asset = models.ForeignKey("Asset")
    manufacturer = models.ForeignKey("manufacturer")
    model = models.CharField(max_length=64)
    size = models.PositiveIntegerField("核数(个)")
    CPUType= models.CharField(max_length=64,verbose_name="CPU型号")
    slot = models.CharField(max_length=32,verbose_name="插槽")
    sn = models.CharField(max_length=128,unique=True)
    statusChoices = (
        (0, '使用中'),
        (1, '出库'),
        (2, '故障'),
        (3, '备用'),
        (4, '过保'),
        (5, '报废'),
        (6, '失联')
    )
    statusName = models.SmallIntegerField(choices=statusChoices)
    class Meta:
        unique_together = ("asset","slot")

class disk(models.Model):
    asset = models.ForeignKey("Asset")
    manufacturer = models.ForeignKey("manufacturer")
    model = models.CharField(max_length=64)
    size = models.PositiveIntegerField("容量(GB)")
    diskType = models.CharField(max_length=64, verbose_name="磁盘类型")
    rangNumber = models.PositiveIntegerField("转数（转）")
    slot = models.CharField(max_length=32,verbose_name="盘位")
    sn = models.CharField(max_length=128,unique=True)
    statusChoices = (
        (0, '使用中'),
        (1, '出库'),
        (2, '故障'),
        (3, '备用'),
        (4, '过保'),
        (5, '报废'),
        (6, '失联')
    )
    statusName = models.SmallIntegerField(choices=statusChoices)
    class Meta:
        unique_together = ("asset", "slot")




# IDC
class IDC(models.Model):
    name = models.CharField(max_length=128,verbose_name="机房名称",unique=True)
    admin = models.CharField(max_length=64, verbose_name="机房负责人")
    contact = models.CharField(max_length=128,verbose_name="机房负责人联系方式")



class rack(models.Model):
    unit = models.ForeignKey("IDCManagementUnit")
    name = models.CharField(max_length=64,verbose_name="机架")
    class Meta:
        unique_together = ("unit","name")

# Network
class Network(models.Model):
    asset = models.OneToOneField('Asset')
    networkChoices = (
        (0,"NetworkDevice"),
        (1,"NetworkLine")
    )
    networkType = models.SmallIntegerField(choices=networkChoices)

class NetworkDevice(models.Model):
    network = models.ForeignKey("Network")
    osName = models.ForeignKey('os')
    oobIP = models.GenericIPAddressField(blank=True, null=True)
    loopbackIP = models.GenericIPAddressField(blank=True, null=True)
    deviceChoices = (
        (0, "路由器"),
        (1, "交换机"),
        (2,"防火墙"),
        (3,"负载均衡")
    )
    deviceType = models.SmallIntegerField(choices=deviceChoices)
    coreChoices = (
        (0,"是")
        (1,"否")
    )
    core = models.SmallIntegerField(choices=coreChoices)

class NetworkLine(models.Model):
    network = models.ForeignKey("Network")
    lineName = models.CharField(max_length=128,verbose_name="链路名称")
    lineType = models.CharField(max_length=128,verbose_name="链路类型")
    lineNumber = models.CharField(max_length=128,unique=True)
    size = models.PositiveIntegerField("带宽（MB）")
    ipCount = models.PositiveIntegerField("公网IP个数（个）")
    wanIP = models.GenericIPAddressField(blank=True,null=True)
    lanIP = models.GenericIPAddressField(blank=True,null=True)
    fromName = models.CharField(max_length=128,verbose_name="源")
    toName = models.CharField(max_length=128,verbose_name="目的")
    portName = models.PositiveIntegerField("端口",blank=True,null=True)

class IDCManagementUnit(models.Model):
    idc = models.ForeignKey("IDC")
    name = models.CharField(max_length=128,verbose_name="机房管理单元",unique=True)
    admin = models.CharField(max_length=64, verbose_name="机房管理单元负责人")
    contact = models.CharField(max_length=128,verbose_name="机房管理单元负责人联系方式")
    class Meta:
        unique_together = ("idc","name")


# Services
class Services(models.Model):
    asset = models.OneToOneField('Asset')
    serviceChoices = (
        (0, "MiddleWare"),
        (1, "DataBase")
    )
    serviceType = models.SmallIntegerField(choices=serviceChoices)

class MiddleWare(models.Model):
    service = models.ForeignKey("Services")
    name = models.CharField(max_length=128,verbose_name="实例名",unique=True)
    hostIP = models.GenericIPAddressField()
    instanceIP = models.GenericIPAddressField(unique=True)
    areaName = models.CharField(max_length=64,verbose_name="网络区域")
    statusChoice = (
        (0,"在线"),
        (1,"准备下线"),
        (2,"故障")
    )
    statusType = models.SmallIntegerField(choices=statusChoice)
    systemName = models.CharField(max_length=128,verbose_name="业务系统")
    warName = models.CharField(max_length=128,verbose_name="war包名")
    memSize = models.PositiveIntegerField("内存容量（GB）")
    lineSize= models.PositiveIntegerField("线程数（个）")
    instanceChoice = (
        (0,"JBOSS"),
        (1,"KAFKA"),
        (2,"REDIS")
    )
    instanceType = models.SmallIntegerField(choices=instanceChoice)



class DataBase(models.Model):
    service = models.ForeignKey("Services")
    hostIP = models.GenericIPAddressField(unique=True)
    statusChoice = (
        (0, "在线"),
        (1, "准备下线"),
        (2, "故障")
    )
    statusType = models.SmallIntegerField(choices=statusChoice)
    systemName = models.CharField(max_length=128, verbose_name="业务系统")
    VIP = models.GenericIPAddressField(unique=True,blank=True,null=True)
    masterIP = models.GenericIPAddressField(unique=True)
    slaveIP = models.GenericIPAddressField(unique=True)
    masterPort = models.PositiveIntegerField("Master端口")
    slavePort = models.PositiveIntegerField("Slave端口")



class business(models.Model):
    parent_unit = models.ForeignKey("self",related_name="P_unit")
    name = models.CharField(max_length=128,verbose_name="所属业务",unique=True)
    class Meta:
        unique_together = ("parent_unit", "name")





# Other
class manufacturer(models.Model):
    name = models.CharField(max_length=64,unique=True)

class department(models.Model):
    name = models.CharField(max_length=64, unique=True)

class owner(models.Model):
    name = models.CharField(max_length=64, unique=True)

class area(models.Model):
    areaChoice = (
        (0,"测试区域"),
        (1,"研发区域"),
        (3,"生产区域")
    )
    area = models.SmallIntegerField(choices=areaChoice)

class networkArea(models.Model):
    networkAreaChoice = (
        (0,'DCN')
    )
    networkArea = models.SmallIntegerField(choices=networkAreaChoice)

class tags(models.Model):
    name = models.CharField(max_length=64,unique=True)