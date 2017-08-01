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
    businessName = models.ManyToManyField("business",blank=True)
    areaName = models.ForeignKey("area")
    idcName = models.ForeignKey("IDC")
    rackName = models.ForeignKey("rack")
    idcManagementUnitName = models.ForeignKey("IDCManagementUnit")
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


class PhysicalMachine(models.Model):
    pass

class VirtualMachine(models.Model):
    pass

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
    server = models.ForeignKey("Server")


# IDC
class IDC(models.Model):
    pass

class rack(models.Model):
    pass

# Network
class Network(models.Model):
    pass

class NetworkDevice(models.Model):
    pass

class NetworkLine(models.Model):
    pass

class IDCManagementUnit(models.Model):
    pass
# Services
class Services(models.Model):
    pass

class MiddleWare(models.Model):
    pass

class DataBase(models.Model):
        pass

class business(models.Model):
    pass



# Other
class manufacturer(models.Model):
    pass

class department(models.Model):
    pass

class owner(models.Model):
    pass

class area(models.Model):
    pass

