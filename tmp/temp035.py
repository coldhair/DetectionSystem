

s = '''
<!--政策法规源码-->
<P><A  href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=32"><FONT><STRONG>疾病预防控制</STRONG></FONT></A></P>
<A  href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=33"><FONT>传染病</FONT></A><SPAN class=pipe><FONT color=#cccccc>|</FONT></SPAN>
<A  href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=34"><FONT>卫生应急</FONT></A><SPAN class=pipe><FONT color=#cccccc>|</FONT></SPAN>
<A  href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=36"><FONT>病媒生物控制</FONT></A>
<P><A  href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=37"><FONT><STRONG>公共卫生</STRONG></FONT></A></P>
<P><A  href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=38"><FONT><STRONG>职业卫生</STRONG></FONT></A></P>
<P><A  href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=39"><FONT><STRONG>健康体检</STRONG></FONT></A></P>
<P><A  href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=40"><FONT><STRONG>资质管理</STRONG></FONT></A></P>


<!--标准规范源码-->
<LI><A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=23"><FONT><STRONG>疾病预防控制</STRONG></FONT></A></LI>
<LI><A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=24"><FONT>传染病</FONT></A><SPAN class=pipe><FONT
        color=#cccccc>|</FONT></SPAN>
    <A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=25"><FONT>卫生应急</FONT></A><SPAN class=pipe><FONT
            color=#cccccc>|</FONT></SPAN>
    <A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=26"><FONT>慢性病</FONT></A><SPAN class=pipe><FONT
            color=#cccccc>|</FONT></SPAN>
    <A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=27"><FONT>病媒生物控制</FONT></A></LI>
<DIV><A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=28"><FONT><STRONG>公共卫生</STRONG></FONT></A></DIV>
<DIV><A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=29"><FONT><STRONG>职业卫生</STRONG></FONT></A></DIV>
<DIV><A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=30"><FONT><STRONG>健康体检</STRONG></FONT></A></DIV>
<DIV><A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=31"><FONT><STRONG>资质管理</STRONG></FONT></A></DIV>




<!--技术服务首页源码-->
<UL>
    <LI>
        <span style="font-family: Webdings; ">%</span>
        <A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=42"><FONT>健康体检</FONT></A></LI>
    <LI><span style="font-family: Webdings; ">%</span>
        <A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=43"><FONT>健康管理</FONT></A></LI>
    <LI><span style="font-family: Webdings; ">%</span>
        <A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=46"><FONT>卫生检验</FONT></A></LI>
    <LI><span style="font-family: Webdings; ">%</span>
        <A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=47"><FONT>病媒生物防制</FONT></A></LI>
    <LI><span style="font-family: Webdings; ">%</span>
        <A href="http://10.112.66.208:94/portal.php?mod=list&amp;catid=48"><FONT>其他卫生技术服务</FONT></A></LI>
    <LI>
        <hr>
    </LI>
    <LI><A title=机构资质 href=""><FONT style="COLOR: #0000ff; FONT-WEIGHT: 900">机构资质</FONT></A></LI>
    <LI><span style="font-family: Webdings; ">%</span>
        <A title=职业健康体检资质 href=""><FONT color=#333333>职业健康体检资质</FONT></A></LI>
    <LI><span style="font-family: Webdings; ">%</span>
        <A title=职业病危害因素检测与评价资质 href=""><FONT color=#333333>职业病危害因素检测与评价资质</FONT></A></LI>
    <LI><span style="font-family: Webdings; ">%</span>
        <A title=其他卫生资质 href=""><FONT color=#333333>其他卫生资质</FONT></A></LI>
</UL>
'''


def strips(matched):
    return matched.group(1)


def strips1(matched):
    return '<LI>' + matched.group(1) + '</LI>'


import re

p = re.sub(r'<FONT>(.*?)</FONT>', strips, s)  # 去掉所有<FONT>空标签
# print(p)
w = re.sub(r'<P>(.*?)</P>', strips1, p)  # 将所有p标签替换为LI标签
# print(w)
m = re.sub(r'<DIV>(.*?)</DIV>', strips1, w)  # 将所有DIV标签替换为LI标签
print(m)
