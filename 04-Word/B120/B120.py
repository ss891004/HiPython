import docx
myDocument=docx.Document('打折商品.docx')
#重新设置Word文件(myDocument)信息
myDocument.core_properties.author='作者：罗帅 罗斌'
myDocument.core_properties.keywords='关键词：Python实战Word案例'
myDocument.core_properties.comments='备注：精彩案例，永久收藏'
myDocument.save('我的Word文件-打折商品.docx')
