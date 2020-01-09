import os

titles = ['1645-massanutten-shenandoah-villas.page', 
'2293-eagle-trace-massanutten.page', 
'2650-eagle-trace-at-kelly-court.page', 
'3640-the-summit-at-massanutten.page', 
'5711-woodstone-at-massanutten.page', 
'puerto-rico-8843-park-royal-homestay.page', 
'c152-regal-vistas.page', 
'dh31-park-royal-homestay-miami.page', 
'dq80-park-royal-homestay-orlando.page', 
'tradewinds-antigua-6850.page', 
'dj71-tradewinds-aquaterra.page', 
'dm53-tradewinds-aqua-terra-at-mandala.page', 
'd965-grand-velas-all-suites.page', 
'dq10-marival-armony-luxury-resort-and-suites.page']

descriptions = ['Massanuttens Shenandoah Villas | Special Offers | RCI.com',
'Eagle Trace at Massanutten | Special Offers | RCI.com',
'Eagle Trace at Killy Court | Special Offers | RCI.com',
'The Summit at Massanutten | Special Offers | RCI.com',
'Woodstone at Massanutten | Special Offers | RCI.com',
'Park Royal Homestay Club Cala by Royal Holiday | Special Offers | RCI.com',
'Regal Vistas at Massanutten | Special Offers | RCI.com',
'Park Royal Homestay Miami Beach by Royal Holiday | Special Offers | RCI.com',
'Park Royal Homestay Miami Beach by Royal Holiday | Special Offers | RCI.com',
'TradeWinds Antigua | Special Offers | RCI.com',
'TradeWinds Antigua | Special Offers | RCI.com',
'Tradewinds Aqua Terra at Mandala Private Island Resort | Special Offers | RCI.com',
'Grand Velas All Suites & Spa Resort Riviera Maya Grand Class | Special Offers | RCI.com',
'Marival Armony Luxury Resort & Suites | Special Offers | RCI.com',]

dcr = ['templatedata/rci/SpecialOffers/data/en_US/north-america/so-post-1645-massanutten-shenandoah.xml', 
'templatedata/rci/SpecialOffers/data/en_US/north-america/so-post-2293-eagletrace-massanutten.xml', 
'templatedata/rci/SpecialOffers/data/en_US/north-america/so-post-2650-eagletree.xml',
'templatedata/rci/SpecialOffers/data/en_US/north-america/so-post-3640-the-summit.xml',
'templatedata/rci/SpecialOffers/data/en_US/north-america/so-post-5711-woodstone-at-massanutten.xml',
'templatedata/rci/SpecialOffers/data/en_US/caribbean/so-post-puerto-rico-8843.xml',
'templatedata/rci/SpecialOffers/data/en_US/north-america/so-post-c152-regal-vistas.xml',
'templatedata/rci/SpecialOffers/data/en_US/north-america/so-post-dh31-park-royal.xml',
'templatedata/rci/SpecialOffers/data/en_US/north-america/so-post-dq80-homestay-orlando.xml',
'templatedata/rci/SpecialOffers/data/en_US/caribbean/so-post-6850-tradewinds-antigua.xml',
'templatedata/rci/SpecialOffers/data/en_US/caribbean/so-post-dj71-tradewinds-aquaterra.xml',
'templatedata/rci/SpecialOffers/data/en_US/australia-south-pacific/so-post-DM53-tradewinds-aqua.xml',
'templatedata/rci/SpecialOffers/data/en_US/mexico/so-post-d965-grand-velas-all-suites.xml',
'templatedata/rci/SpecialOffers/data/en_US/mexico/so-post-marival-dq10-luxury-resorts.xml',
]

s = """<?xml version="1.0" encoding="UTF-8"?>

<Page ID="1574624268869" Version="3.1.1.0" Private="false" Template="false">
  <Description/>
  <IsMobile>false</IsMobile>
  <Version>0</Version>
  <InternalProperties/>
  <PageTemplates>
    <PageTemplate ID="1" Version="5" PageEditVisibility="visible">
      <Description/>
      <Name>B10 - Special Offers Detail</Name>
      <VPath><![CDATA[RCI/B10 - Special Offers Detail.template]]></VPath>
    </PageTemplate>
  </PageTemplates>
  <Page_Display_Properties Class="com.interwoven.livesite.model.page.PageProperties">
    <Title>%s</Title>
    <BGColor/>
    <Background/>
    <Center>false</Center>
    <Width/>
    <PageType>
      <Id>htmlQuirksMode</Id>
      <Layout canvas-path="B10 - Special Offers Detail.xml">fixed-layout</Layout>
      <EmbeddedLayout><![CDATA[]]></EmbeddedLayout>
    </PageType>
    <Description>View details of this Special Offer from RCI.</Description>
    <Keywords>special offers, special deals, resort deals, resort offers, resort discounts, sale, promotion, deal, deals, cheap,  all-inclusive, all 

inclusive, details, destination, Mexico, San Miguel de Allende, Guanajauto, reduced travel, online offers, online deals, holiday offers, holiday, last minute, minute deals, minute, 

hotels, hotel specials, timeshare, vacation, vacation ownership, family, resorts, coupons, resort coupons, vacation certificate,  RCI, 

RCI.com,</Keywords>
    <Urls/>
    <Controllers>
      <Pre/>
      <Post/>
    </Controllers>
    <Resources>
      <Resource Type="0" Enabled="true" IsSiteResource="false" MimeType="text/css">
        <Path>static/css/specialOffers/special-offers.css</Path>
        <Devices/>
      </Resource>
      <Resource Type="1" Enabled="true" IsSiteResource="false" MimeType="text/javascript">
        <Path>static/js/jquery/jquery.matchHeight-min.js</Path>
        <Devices/>
      </Resource>
    </Resources>
    <MetaTags/>
  </Page_Display_Properties>
  <Page_Content>
    <Component ID="1574624268870" Version="3.1.1.0" PageID="1" TemplateComponentID="1429034850016" CanBeActive="true" Checksum="22beeb3db98e9926cc1e3b36d5d87bb64a3611df">
      <Description/>
      <SelectedSkin Changed="true">S-1: Logged In</SelectedSkin>
      <DisplayName>Header</DisplayName>
      <Name>Header</Name>
      <IsMobileComponent>false</IsMobileComponent>
      <BaseComponent Version="27"><![CDATA[Header - Footer/Header.component]]></BaseComponent>
      <ContainerProperties ID="1429034850022" locked="false">
        <FixedLayoutArea ID="row-1-area-1" index="0"/>
        <CacheTime>0</CacheTime>
        <BGColor/>
        <Width>200</Width>
        <Height>200</Height>
        <Top>10</Top>
        <Left>10</Left>
        <ZIndex>0</ZIndex>
        <RenderInRuntime>true</RenderInRuntime>
        <JavascriptCallback/>
        <WidthType/>
        <HeightType/>
        <WidthPercent/>
      </ContainerProperties>
      <InternalProperties/>
      <Locks>
        <ContainerProperties locked="false" Changed="false"/>
        <Properties locked="false" Changed="false"/>
        <Data locked="false" Changed="false"/>
      </Locks>
      <Segments>
        <Segment ID="0">
          <Properties ComponentID="1574624268870"/>
          <Data>
            <External>
              <Parameters>
                <Datum ID="E01-D01" Name="Session Attribute Name" Type="String" Exposed="false">MemberAttributes</Datum>
                <Datum ID="E01-D02" Name="DCR Type" Type="String" Exposed="false">rci/Header</Datum>
                <Datum ID="E01-D03" Name="Content ID" Type="String" Exposed="false"/>
                <Datum ID="E01-D99" Name="Rules Selection" Type="SelectMultiple">
                  <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                </Datum>
                <Datum ID="E01-D07" Name="Max Results" Type="Number">1</Datum>
                <Datum ID="E01-D08" Name="Score Results" Type="Boolean" Exposed="false">false</Datum>
                <Datum ID="E01-D09" Name="Response Root Node" Type="String" Exposed="false">documents</Datum>
                <Datum ID="E01-D10" Name="Response Param Node" Type="String" Exposed="false">document</Datum>
                <Datum ID="E01-D11" Name="Property Map Path" Type="String" Exposed="false"/>
                <Group ID="E01-G01" Name="Default Rules Values" Replicatable="true" CloneGroupID="hixbduq1">
                  <Datum Changed="true" ID="E01-G01-D01" Name="Rule Name" Type="SelectSingle">
                    <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                    <Option Selected="true">
                      <Display>Application Type</Display>
                      <Value>Application Type</Value>
                    </Option>
                  </Datum>
                  <Datum ID="E01-G01-D02" Name="Rule Value" Type="String"/>
                </Group>
                <Datum Changed="true" ID="E01-D12" Name="Default Document" Type="DCR">
                  <DCR Category="rci" Type="Header">templatedata/rci/Header/data/en_US/club-wvr-header.xml</DCR>
                </Datum>
              </Parameters>
              <Object Scope="local">com.rci.livesite.targeting.HeaderContentRetriever</Object>
              <Method>getTargetedContent</Method>
            </External>
          </Data>
        </Segment>
      </Segments>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-3: Slim Post Login </Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;

    &lt;!-- Skin: Slim Logged In --&gt;
    &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/c01-s3-slim-post-login-header.xsl" /&gt;

&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="true" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-1: Logged In</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Logged In --&gt;
 
  &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/c01-s3-post-login-header.xsl" /&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-2: Pre Login </Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Pre Login Cookie --&gt;

  &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/pre-login-header-cookie.xsl" /&gt;
 &lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S2: Pre login - right</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Pre Login Cookie --&gt;

  &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/pre-login-header-sign-in-right-cookie.xsl" /&gt;
 &lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-1: Logged In Ice</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Logged In --&gt;

  &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/c01-s3-post-login-header-ice.xsl" /&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
    </Component>
    <Component ID="1574624268871" Version="3.1.1.0" PageID="1" TemplateComponentID="1429034850017" CanBeActive="true" Checksum="df589e4c09814056254fbce9835ef0cbfd2dfee7">
      <Description/>
      <SelectedSkin>S-1:Special Offer Detail </SelectedSkin>
      <DisplayName>Special Offers Detail</DisplayName>
      <Name>Special Offers Detail</Name>
      <IsMobileComponent>false</IsMobileComponent>
      <BaseComponent Version="3"><![CDATA[Special Offers/Special Offers Detail.component]]></BaseComponent>
      <ContainerProperties ID="1429034850023" locked="false">
        <FixedLayoutArea ID="row-2-area-1" index="1"/>
        <CacheTime>0</CacheTime>
        <BGColor/>
        <Width>0</Width>
        <Height>0</Height>
        <Top>0</Top>
        <Left>0</Left>
        <ZIndex>0</ZIndex>
        <RenderInRuntime>true</RenderInRuntime>
        <JavascriptCallback/>
        <WidthType/>
        <HeightType/>
        <WidthPercent/>
      </ContainerProperties>
      <InternalProperties/>
      <Locks>
        <ContainerProperties locked="false" Changed="false"/>
        <Properties locked="false" Changed="false"/>
        <Data locked="false" Changed="false"/>
      </Locks>
      <Segments>
        <Segment ID="0">
          <Properties ComponentID="1574624268871">
            <Datum ID="Icon-Style" Type="SelectSingle" Name="Icon Style">
              <Option Selected="true">
                <Display>Clock</Display>
                <Value>limited-time</Value>
              </Option>
            </Datum>
          </Properties>
          <Data>
            <Datum Changed="true" ID="Labels" Name="Labels DCR" Type="DCR">
              <DCR Category="rci" Type="Labels">templatedata/rci/Labels/data/en_US/wvr-club-labels.xml</DCR>
            </Datum>
            <External>
              <Parameters>
                <Datum ID="E01-D01" Name="Session Attribute Name" Type="String" Exposed="false">MemberAttributes</Datum>
                <Datum ID="E01-D02" Name="DCR Type" Type="String" Exposed="false">rci/SpecialOffers</Datum>
                <Datum ID="E01-D03" Name="Content ID" Type="String" Exposed="false"/>
                <Datum ID="E01-D99" Name="Rules Selection" Type="SelectMultiple">
                  <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                </Datum>
                <Datum ID="E01-D14" Name="Location" Type="SelectSingle" Changed="true">
                  <Generator Object="com.rci.livesite.external.LocationOptionGenerator" Method="getOptions">
                    <Parameters>
                      <Datum ID="E01-D14-G01" Name="XML Source" Type="String" Exposed="false">/iwadmin/main/rci/data/STAGING/templatedata/CustomData/OptionList/data/special-offers-loc.xml</Datum>
                    </Parameters>
                  </Generator>
                  <Option Selected="true">
                    <Display>None</Display>
                    <Value/>
                  </Option>
                </Datum>
                <Datum ID="E01-D13" Name="Honor Publication Dates" Type="Boolean">false</Datum>
                <Datum ID="E01-D07" Name="Max Results" Type="Number">1</Datum>
                <Datum ID="E01-D08" Name="Score Results" Type="Boolean" Exposed="false">false</Datum>
                <Datum ID="E01-D09" Name="Response Root Node" Type="String" Exposed="false">documents</Datum>
                <Datum ID="E01-D10" Name="Response Param Node" Type="String" Exposed="false">document</Datum>
                <Datum ID="E01-D11" Name="Property Map Path" Type="String" Exposed="false"/>
                <Group ID="E01-G01" Name="Default Rules Values" Replicatable="true" CloneGroupID="hixbduq1">
                  <Datum Changed="true" ID="E01-G01-D01" Name="Rule Name" Type="SelectSingle">
                    <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                    <Option Selected="true">
                      <Display>Active PrePaid Cert Owner</Display>
                      <Value>Active PrePaid Cert Owner</Value>
                    </Option>
                  </Datum>
                  <Datum ID="E01-G01-D02" Name="Rule Value" Type="String"/>
                </Group>
                <Datum Changed="true" ID="E01-D12" Name="Default Document" Type="DCR">
                  <DCR Category="rci" Type="SpecialOffers">%s</DCR>
                </Datum>
              </Parameters>
              <Object Scope="local">com.rci.livesite.targeting.ContentRetriever</Object>
              <Method>getTargetedContent</Method>
            </External>
          </Data>
        </Segment>
      </Segments>
      <Stylesheet Default="true" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-1:Special Offer Detail </Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Default XSL --&gt;

&lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/rci-special-offers/c50-s1-special-offers-detail-main.xsl" /&gt; 



&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
    </Component>
    <Component ID="1574624268872" Version="3.1.1.0" PageID="1" TemplateComponentID="1429034850462" CanBeActive="true" Checksum="177cb87486b518581ec372cfdbdf122ecf4310fe">
      <Description/>
      <SelectedSkin>S-1: Four Column</SelectedSkin>
      <DisplayName>Link List Sitemap</DisplayName>
      <Name>Link List Sitemap</Name>
      <IsMobileComponent>false</IsMobileComponent>
      <BaseComponent Version="4"><![CDATA[Special Offers/Link List Sitemap.component]]></BaseComponent>
      <ContainerProperties ID="0" locked="false">
        <FixedLayoutArea ID="row-2-area-3" index="0"/>
        <CacheTime>0</CacheTime>
        <BGColor/>
        <Width>200</Width>
        <Height>200</Height>
        <Top>10</Top>
        <Left>10</Left>
        <ZIndex>0</ZIndex>
        <RenderInRuntime>true</RenderInRuntime>
        <JavascriptCallback/>
        <WidthType/>
        <HeightType/>
        <WidthPercent/>
      </ContainerProperties>
      <InternalProperties/>
      <Locks>
        <ContainerProperties locked="false" Changed="false"/>
        <Properties locked="false" Changed="false"/>
        <Data locked="false" Changed="false"/>
      </Locks>
      <Segments>
        <Segment ID="0">
          <Properties ComponentID="1574624268872"/>
          <Data>
            <External>
              <Parameters>
                <Datum ID="E01-D01" Name="Session Attribute Name" Type="String" Exposed="false">MemberAttributes</Datum>
                <Datum ID="E01-D02" Name="DCR Type" Type="String" Exposed="false">rci/ListOfLinks</Datum>
                <Datum ID="E01-D03" Name="Content ID" Type="String" Exposed="false"/>
                <Datum ID="E01-D99" Name="Rules Selection" Type="SelectMultiple">
                  <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                </Datum>
                <Datum ID="E01-D14" Name="Location" Type="SelectSingle">
                  <Generator Object="com.rci.livesite.external.LocationOptionGenerator" Method="getOptions">
                    <Parameters>
                      <Datum ID="E01-D14-G01" Name="XML Source" Type="String" Exposed="false">/iwadmin/main/rci/data/STAGING/templatedata/CustomData/OptionList/data/listoflinks-loc.xml</Datum>
                    </Parameters>
                  </Generator>
                  <Option Selected="true">
                    <Display/>
                    <Value/>
                  </Option>
                </Datum>
                <Datum ID="E01-D13" Name="Honor Publication Dates" Type="Boolean">false</Datum>
                <Datum ID="E01-D07" Name="Max Results" Type="Number">1</Datum>
                <Datum ID="E01-D08" Name="Score Results" Type="Boolean" Exposed="false">false</Datum>
                <Datum ID="E01-D09" Name="Response Root Node" Type="String" Exposed="false">documents</Datum>
                <Datum ID="E01-D10" Name="Response Param Node" Type="String" Exposed="false">document</Datum>
                <Datum ID="E01-D11" Name="Property Map Path" Type="String" Exposed="false"/>
                <Group ID="E01-G01" Name="Default Rules Values" Replicatable="true" CloneGroupID="hixbduq1">
                  <Datum Changed="true" ID="E01-G01-D01" Name="Rule Name" Type="SelectSingle">
                    <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                    <Option Selected="true">
                      <Display>Active PrePaid Cert Owner</Display>
                      <Value>Active PrePaid Cert Owner</Value>
                    </Option>
                  </Datum>
                  <Datum ID="E01-G01-D02" Name="Rule Value" Type="String"/>
                </Group>
                <Datum Changed="true" ID="E01-D12" Name="Default Document" Type="DCR">
                  <DCR Category="rci" Type="ListOfLinks">templatedata/rci/ListOfLinks/data/en_US/special-offers/pow-special-offers-footer-listoflinks.xml</DCR>
                </Datum>
              </Parameters>
              <Object Scope="local">com.rci.livesite.targeting.ContentRetriever</Object>
              <Method>getTargetedContent</Method>
            </External>
          </Data>
        </Segment>
      </Segments>
      <Stylesheet Default="true" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-1: Four Column</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Default XSL --&gt;

  &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/rci-special-offers/c21-s1-list-of-links.xsl" /&gt; 
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
    </Component>
    <Component ID="1574624268873" Version="3.1.1.0" PageID="1" TemplateComponentID="1429034850464" CanBeActive="true" Checksum="8c80de93b65aba66f5f26e3226a174c1d50a3c83">
      <Description/>
      <SelectedSkin Changed="true">S-2: Post Login</SelectedSkin>
      <DisplayName>Footer</DisplayName>
      <Name>Footer</Name>
      <IsMobileComponent>false</IsMobileComponent>
      <BaseComponent Version="12"><![CDATA[Header - Footer/Footer.component]]></BaseComponent>
      <ContainerProperties ID="0" locked="false">
        <FixedLayoutArea ID="row-3-area-1" index="0"/>
        <CacheTime>0</CacheTime>
        <BGColor/>
        <Width>200</Width>
        <Height>200</Height>
        <Top>10</Top>
        <Left>10</Left>
        <ZIndex>0</ZIndex>
        <RenderInRuntime>true</RenderInRuntime>
        <JavascriptCallback/>
        <WidthType/>
        <HeightType/>
        <WidthPercent/>
      </ContainerProperties>
      <InternalProperties/>
      <Locks>
        <ContainerProperties locked="false" Changed="false"/>
        <Properties locked="false" Changed="false"/>
        <Data locked="false" Changed="false"/>
      </Locks>
      <Segments>
        <Segment ID="0">
          <Properties ComponentID="1574624268873"/>
          <Data>
            <External>
              <Parameters>
                <Datum ID="E01-D01" Name="Session Attribute Name" Type="String" Exposed="false">MemberAttributes</Datum>
                <Datum ID="E01-D02" Name="DCR Type" Type="String" Exposed="false">rci/Footer</Datum>
                <Datum ID="E01-D03" Name="Content ID" Type="String" Exposed="false"/>
                <Datum ID="E01-D99" Name="Rules Selection" Type="SelectMultiple">
                  <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                </Datum>
                <Datum ID="E01-D07" Name="Max Results" Type="Number">1</Datum>
                <Datum ID="E01-D08" Name="Score Results" Type="Boolean" Exposed="false">false</Datum>
                <Datum ID="E01-D09" Name="Response Root Node" Type="String" Exposed="false">documents</Datum>
                <Datum ID="E01-D10" Name="Response Param Node" Type="String" Exposed="false">document</Datum>
                <Datum ID="E01-D11" Name="Property Map Path" Type="String" Exposed="false"/>
                <Group ID="E01-G01" Name="Default Rules Values" Replicatable="true" CloneGroupID="hixbduq1">
                  <Datum Changed="true" ID="E01-G01-D01" Name="Rule Name" Type="SelectSingle">
                    <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                    <Option Selected="true">
                      <Display>Application Type</Display>
                      <Value>Application Type</Value>
                    </Option>
                  </Datum>
                  <Datum ID="E01-G01-D02" Name="Rule Value" Type="String"/>
                </Group>
                <Datum Changed="true" ID="E01-D12" Name="Default Document" Type="DCR">
                  <DCR Category="rci" Type="Footer">templatedata/rci/Footer/data/en_US/club-wvr-footer.xml</DCR>
                </Datum>
              </Parameters>
              <Object Scope="local">com.rci.livesite.targeting.ContentRetriever</Object>
              <Method>getTargetedContent</Method>
            </External>
          </Data>
        </Segment>
      </Segments>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-2: Post Login</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: c02-s2-post-login-footer --&gt;

 &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/post-login-footer.xsl" /&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="true" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-1: Pre Login</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: c01-s1-pre-login-footer --&gt;

  &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/pre-login-footer.xsl" /&gt;
 &lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>Default</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Default XSL --&gt;


  &lt;xsl:template match="/"&gt;
 &lt;div id="fb-root"&gt;&lt;/div&gt;
	&lt;script&gt;
		(function(d, s, id) {
			var js, fjs = d.getElementsByTagName(s)[0];
			if (d.getElementById(id)) return;
			js = d.createElement(s); js.id = id;
			js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
			fjs.parentNode.insertBefore(js, fjs);
		}(document, 'script', 'facebook-jssdk'));
	&lt;/script&gt;

	&lt;!-- Page Layout 
    ================================================== --&gt;   
	&lt;!-- Footer
    ================================================== --&gt;
    &lt;footer class="c2"&gt;
  &lt;div class="container"&gt;
    &lt;div class="footer-links"&gt;
      &lt;div class="row"&gt;  
        &lt;div class="span12"&gt;
          &lt;div class="row"&gt;
            &lt;div class="span12"&gt;              
              &lt;ul class="nav footer-nav"&gt;
                &lt;li class="first"&gt;&lt;a href="#"&gt;About RCI&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;RCI Affiliates&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Careers&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;University Relations&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Contact Us&lt;/a&gt;&lt;/li&gt;
                &lt;li class="last"&gt;&lt;a href="#"&gt;Terms of Use&lt;/a&gt;&lt;/li&gt;     
              &lt;/ul&gt;
              &lt;ul class="nav footer-nav"&gt;
                &lt;li class="first"&gt;&lt;a href="#"&gt;Legal Notices&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Cookie Law&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Privacy Policy&lt;/a&gt;&lt;/li&gt;
                &lt;li class="last"&gt;&lt;a href="#"&gt;Connect with RCI&lt;/a&gt;&lt;/li&gt;       
              &lt;/ul&gt;              
            &lt;/div&gt;            
          &lt;/div&gt;
        &lt;/div&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/div&gt;
  &lt;div class="social-buttons"&gt;
    &lt;div class="container"&gt;
      &lt;div class="row"&gt;  
        &lt;div class="span12"&gt;
          &lt;ul class="nav social-nav pull-right"&gt;
            &lt;li&gt;
              &lt;a href="#"&gt;&lt;i class="icon-facebook"&gt;&lt;/i&gt;&lt;/a&gt;
            &lt;/li&gt;
            &lt;li&gt;
              &lt;a href="#"&gt;&lt;i class="icon-twitter"&gt;&lt;/i&gt;&lt;/a&gt;
            &lt;/li&gt;
            &lt;li&gt;
              &lt;a href="#"&gt;&lt;i class="icon-youtube"&gt;&lt;/i&gt;&lt;/a&gt;
            &lt;/li&gt;
            &lt;li&gt;
              &lt;a href="#"&gt;&lt;i class="icon-rss"&gt;&lt;/i&gt;&lt;/a&gt;
            &lt;/li&gt;            
            &lt;li&gt;
              &lt;a href="#"&gt;&lt;i class="icon-rci-tv"&gt;&lt;/i&gt;&lt;/a&gt;
            &lt;/li&gt;
            &lt;li&gt;&lt;div class="fb-like" data-send="false" data-width="165" data-show-faces="false"&gt;&lt;/div&gt;&lt;/li&gt;
            &lt;/ul&gt;
          &lt;/div&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/footer&gt;
  &lt;/xsl:template&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
    </Component>
    <Component ID="1574624268874" Version="3.1.1.0" PageID="1" TemplateComponentID="1429034850782" CanBeActive="true" Checksum="2ab372a03dfe4d784d42b4c1aa2c535ce65c798d">
      <Description/>
      <SelectedSkin>Default</SelectedSkin>
      <DisplayName>WYSIWYG - HTML</DisplayName>
      <Name>WYSIWYG - HTML</Name>
      <IsMobileComponent>false</IsMobileComponent>
      <BaseComponent Version="9"><![CDATA[Manual - DCR Browse/WYSIWYG - HTML.component]]></BaseComponent>
      <ContainerProperties ID="0" locked="false">
        <FixedLayoutArea ID="row-1-area-1" index="1"/>
        <CacheTime>-1</CacheTime>
        <BGColor/>
        <Width>1176</Width>
        <Height>987</Height>
        <Top>10</Top>
        <Left>10</Left>
        <ZIndex>0</ZIndex>
        <RenderInRuntime>true</RenderInRuntime>
        <JavascriptCallback/>
        <WidthType/>
        <HeightType/>
        <WidthPercent/>
      </ContainerProperties>
      <InternalProperties/>
      <Locks>
        <ContainerProperties locked="false" Changed="false"/>
        <Properties locked="false" Changed="false"/>
        <Data locked="false" Changed="false"/>
      </Locks>
      <Segments>
        <Segment ID="0">
          <Properties ComponentID="1574624268874"/>
          <Data>
            <Datum Changed="true" ID="DCR" Name="DCR" Type="DCR">
              <DCR Category="rci" Type="GenericHTML">templatedata/rci/GenericHTML/data/en_US/special-offers/special-offers-header.xml</DCR>
            </Datum>
          </Data>
        </Segment>
      </Segments>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="html">
        <Name>skin - t4</Name>
        <XSL>&lt;article class="t4 content-item"&gt;
$MODEL{/Properties/Data/Datum[@Name='DCR']/DCR/WYSIWYG/GenericHTML/Content}
&lt;/article&gt;
</XSL>      </Stylesheet>      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="html">        <Name>skin - t5</Name>
        <XSL>&lt;article class="t3 content-item"&gt;
$MODEL{/Properties/Data/Datum[@Name='DCR']/DCR/WYSIWYG/GenericHTML/Content}
&lt;/article&gt;        
    </XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="html">
        <Name>skin - t2</Name>
        <XSL>&lt;article class="t2 content-item"&gt;
$MODEL{/Properties/Data/Datum[@Name='DCR']/DCR/WYSIWYG/GenericHTML/Content}
&lt;/article&gt;         
    </XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="html">
        <Name>skin - t3</Name>
        <XSL>&lt;article class="t3 content-item"&gt;
$MODEL{/Properties/Data/Datum[@Name='DCR']/DCR/WYSIWYG/GenericHTML/Content}
&lt;/article&gt;
         
    </XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="html">
        <Name>skin - t1</Name>
        <XSL>&lt;article class="t1 content-item"&gt;
$MODEL{/Properties/Data/Datum[@Name='DCR']/DCR/WYSIWYG/GenericHTML/Content}
&lt;/article&gt;

       
    </XSL>
      </Stylesheet>
      <Stylesheet Default="true" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="html">
        <Name>Default</Name>
        <XSL>   $MODEL{/Properties/Data/Datum[@Name='DCR']/DCR/WYSIWYG/GenericHTML/Content}
</XSL>      </Stylesheet>      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="html">        <Name>skin - t6</Name>
        <XSL>&lt;article class="t6 content-item"&gt;
$MODEL{/Properties/Data/Datum[@Name='DCR']/DCR/WYSIWYG/GenericHTML/Content}
&lt;/article&gt;  </XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="html">
        <Name>skin - t7</Name>
        <XSL>&lt;article class="t7 content-item"&gt;
$MODEL{/Properties/Data/Datum[@Name='DCR']/DCR/WYSIWYG/GenericHTML/Content}
&lt;/article&gt;          
    </XSL>
      </Stylesheet>
    </Component>
    <Component ID="1574624268875" Version="3.1.1.0" PageID="0" TemplateComponentID="0" CanBeActive="true" Checksum="44a7060783c25475c0ee4e2227dea77a3bc124c2">
      <Description/>
      <SelectedSkin Changed="true">S-1: Vertical Short</SelectedSkin>
      <DisplayName>Rules Based Offer</DisplayName>
      <Name>Rules Based Offer</Name>
      <IsMobileComponent>false</IsMobileComponent>
      <BaseComponent Version="40"><![CDATA[Targeted - Rules Based/Rules Based Offer.component]]></BaseComponent>
      <ContainerProperties ID="0" locked="false">
        <FixedLayoutArea ID="row-2-area-2" index="0"/>
        <CacheTime>0</CacheTime>
        <BGColor/>
        <Width>200</Width>
        <Height>200</Height>
        <Top>10</Top>
        <Left>10</Left>
        <ZIndex>0</ZIndex>
        <RenderInRuntime>true</RenderInRuntime>
        <JavascriptCallback/>
        <WidthType/>
        <HeightType/>
        <WidthPercent/>
      </ContainerProperties>
      <InternalProperties/>
      <Locks>
        <ContainerProperties locked="false" Changed="false"/>
        <Properties locked="false" Changed="false"/>
        <Data locked="false" Changed="false"/>
      </Locks>
      <Segments>
        <Segment ID="0">
          <Properties ComponentID="1574624268875"/>
          <Data>
            <External>
              <Parameters>
                <Datum ID="E01-D01" Name="Session Attribute Name" Type="String" Exposed="false">MemberAttributes</Datum>
                <Datum ID="E01-D02" Name="DCR Type" Type="String" Exposed="false">rci/Offers</Datum>
                <Datum ID="E01-D03" Name="Content ID" Type="String" Exposed="false"/>
                <Datum ID="E01-D99" Name="Rules Selection" Type="SelectMultiple">
                  <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                </Datum>
                <Datum ID="E01-D14" Name="Location" Type="SelectSingle">
                  <Option Selected="true">
                    <Display>None</Display>
                    <Value/>
                  </Option>
                  <Option>
                    <Display>allinclusive_first center banner_c5</Display>
                    <Value>b6_c5_a_allinclusive</Value>
                  </Option>
                  <Option>
                    <Display>allinclusive_second center banner_c5</Display>
                    <Value>b6_c5_b_allinclusive</Value>
                  </Option>
                  <Option>
                    <Display>artsmuseums_first center banner_c5</Display>
                    <Value>b6_c5_a_artsmuseums</Value>
                  </Option>
                  <Option>
                    <Display>artsmuseums_second center banner_c5</Display>
                    <Value>b6_c5_b_artsmuseums</Value>
                  </Option>
                  <Option>
                    <Display>aruba_first center banner_c5</Display>
                    <Value>b5_c5_b_aruba</Value>
                  </Option>
                  <Option>
                    <Display>aruba_header banner_c5</Display>
                    <Value>b5_c5_a_aruba</Value>
                  </Option>
                  <Option>
                    <Display>aruba_second center banner_c5</Display>
                    <Value>b5_c5_c_aruba</Value>
                  </Option>
                  <Option>
                    <Display>attractions_first center banner_c5</Display>
                    <Value>b6_c5_a_attractions</Value>
                  </Option>
                  <Option>
                    <Display>attractions_second center banner_c5</Display>
                    <Value>b6_c5_b_attractions</Value>
                  </Option>
                  <Option>
                    <Display>beaches_first center banner_c5</Display>
                    <Value>b6_c5_a_beaches</Value>
                  </Option>
                  <Option>
                    <Display>beaches_second center banner_c5</Display>
                    <Value>b6_c5_b_beaches</Value>
                  </Option>
                  <Option>
                    <Display>bransonarea_first center banner_c5</Display>
                    <Value>b5_c5_b_bransonarea</Value>
                  </Option>
                  <Option>
                    <Display>bransonarea_header banner_c5</Display>
                    <Value>b5_c5_a_bransonarea</Value>
                  </Option>
                  <Option>
                    <Display>bransonarea_second center banner_c5</Display>
                    <Value>b5_c5_c_bransonarea</Value>
                  </Option>
                  <Option>
                    <Display>canadianrockies_first center banner_c5</Display>
                    <Value>b5_c5_b_canadianrockies</Value>
                  </Option>
                  <Option>
                    <Display>canadianrockies_header banner_c5</Display>
                    <Value>b5_c5_a_canadianrockies</Value>
                  </Option>
                  <Option>
                    <Display>canadianrockies_second center banner_c5</Display>
                    <Value>b5_c5_c_canadianrockies</Value>
                  </Option>
                  <Option>
                    <Display>cancun_first center banner_c5</Display>
                    <Value>b5_c5_b_cancun</Value>
                  </Option>
                  <Option>
                    <Display>cancun_header banner_c5</Display>
                    <Value>b5_c5_a_cancun</Value>
                  </Option>
                  <Option>
                    <Display>cancun_second center banner_c5</Display>
                    <Value>b5_c5_c_cancun</Value>
                  </Option>
                  <Option>
                    <Display>capecod_first center banner_c5</Display>
                    <Value>b5_c5_b_capecod</Value>
                  </Option>
                  <Option>
                    <Display>capecod_header banner_c5</Display>
                    <Value>b5_c5_a_capecod</Value>
                  </Option>
                  <Option>
                    <Display>capecod_second center banner_c5</Display>
                    <Value>b5_c5_c_capecod</Value>
                  </Option>
                  <Option>
                    <Display>colorado_first center banner_c5</Display>
                    <Value>b5_c5_b_colorado</Value>
                  </Option>
                  <Option>
                    <Display>colorado_header banner_c5</Display>
                    <Value>b5_c5_a_colorado</Value>
                  </Option>
                  <Option>
                    <Display>colorado_second center banner_c5</Display>
                    <Value>b5_c5_c_colorado</Value>
                  </Option>
                  <Option>
                    <Display>cruise_first center banner_c5</Display>
                    <Value>b6_c5_a_cruise</Value>
                  </Option>
                  <Option>
                    <Display>cruise_second center banner_c5</Display>
                    <Value>b6_c5_b_cruise</Value>
                  </Option>
                  <Option>
                    <Display>dining_first center banner_c5</Display>
                    <Value>b6_c5_a_dining</Value>
                  </Option>
                  <Option>
                    <Display>dining_second center banner_c5</Display>
                    <Value>b6_c5_b_dining</Value>
                  </Option>
                  <Option>
                    <Display>dominicanrepublic_first center banner_c5</Display>
                    <Value>b5_c5_b_dominicanrepublic</Value>
                  </Option>
                  <Option>
                    <Display>dominicanrepublic_header banner_c5</Display>
                    <Value>b5_c5_a_dominicanrepublic</Value>
                  </Option>
                  <Option>
                    <Display>dominicanrepublic_second center banner_c5</Display>
                    <Value>b5_c5_c_dominicanrepublic</Value>
                  </Option>
                  <Option>
                    <Display>family_first center banner_c5</Display>
                    <Value>b6_c5_a_family</Value>
                  </Option>
                  <Option>
                    <Display>family_second center banner_c5</Display>
                    <Value>b6_c5_b_family</Value>
                  </Option>
                  <Option>
                    <Display>flnorthernatlanticcoast_first center banner_c5</Display>
                    <Value>b5_c5_b_flnorthernatlanticcoast</Value>
                  </Option>
                  <Option>
                    <Display>flnorthernatlanticcoast_header banner_c5</Display>
                    <Value>b5_c5_a_flnorthernatlanticcoast</Value>
                  </Option>
                  <Option>
                    <Display>flnorthernatlanticcoast_second center banner_c5</Display>
                    <Value>b5_c5_c_flnorthernatlanticcoast</Value>
                  </Option>
                  <Option>
                    <Display>flpanhandle_first center banner_c5</Display>
                    <Value>b5_c5_b_flpanhandle</Value>
                  </Option>
                  <Option>
                    <Display>flpanhandle_header banner_c5</Display>
                    <Value>b5_c5_a_flpanhandle</Value>
                  </Option>
                  <Option>
                    <Display>flpanhandle_second center banner_c5</Display>
                    <Value>b5_c5_c_flpanhandle</Value>
                  </Option>
                  <Option>
                    <Display>golf_first center banner_c5</Display>
                    <Value>b6_c5_a_golf</Value>
                  </Option>
                  <Option>
                    <Display>golf_second center banner_c5</Display>
                    <Value>b6_c5_b_golf</Value>
                  </Option>
                  <Option>
                    <Display>helphome_banner_c5</Display>
                    <Value>a7_c5_a_helphome</Value>
                  </Option>
                  <Option>
                    <Display>hiltonhead_first center banner_c5</Display>
                    <Value>b5_c5_b_hiltonhead</Value>
                  </Option>
                  <Option>
                    <Display>hiltonhead_header banner_c5</Display>
                    <Value>b5_c5_a_hiltonhead</Value>
                  </Option>
                  <Option>
                    <Display>hiltonhead_second center banner_c5</Display>
                    <Value>b5_c5_c_hiltonhead</Value>
                  </Option>
                  <Option>
                    <Display>historic_first center banner_c5</Display>
                    <Value>b6_c5_a_historic</Value>
                  </Option>
                  <Option>
                    <Display>historic_second center banner_c5</Display>
                    <Value>b6_c5_b_historic</Value>
                  </Option>
                  <Option>
                    <Display>holidays_first center banner_c5</Display>
                    <Value>b6_c5_a_holidays</Value>
                  </Option>
                  <Option>
                    <Display>holidays_second center banner_c5</Display>
                    <Value>b6_c5_b_holidays</Value>
                  </Option>
                  <Option>
                    <Display>kauai_first center banner_c5</Display>
                    <Value>b5_c5_b_kauai</Value>
                  </Option>
                  <Option>
                    <Display>kauai_header banner_c5</Display>
                    <Value>b5_c5_a_kauai</Value>
                  </Option>
                  <Option>
                    <Display>kauai_second center banner_c5</Display>
                    <Value>b5_c5_c_kauai</Value>
                  </Option>
                  <Option>
                    <Display>laketahoe_first center banner_c5</Display>
                    <Value>b5_c5_b_laketahoe</Value>
                  </Option>
                  <Option>
                    <Display>laketahoe_header banner_c5</Display>
                    <Value>b5_c5_a_laketahoe</Value>
                  </Option>
                  <Option>
                    <Display>laketahoe_second center banner_c5</Display>
                    <Value>b5_c5_c_laketahoe</Value>
                  </Option>
                  <Option>
                    <Display>lasvegas_first center banner_c5</Display>
                    <Value>b5_c5_b_lasvegas</Value>
                  </Option>
                  <Option>
                    <Display>lasvegas_header banner_c5</Display>
                    <Value>b5_c5_a_lasvegas</Value>
                  </Option>
                  <Option>
                    <Display>lasvegas_second center banner_c5</Display>
                    <Value>b5_c5_c_lasvegas</Value>
                  </Option>
                  <Option>
                    <Display>loscabos_first center banner_c5</Display>
                    <Value>b5_c5_b_loscabos</Value>
                  </Option>
                  <Option>
                    <Display>loscabos_header banner_c5</Display>
                    <Value>b5_c5_a_loscabos</Value>
                  </Option>
                  <Option>
                    <Display>loscabos_second center banner_c5</Display>
                    <Value>b5_c5_c_loscabos</Value>
                  </Option>
                  <Option>
                    <Display>massanutten_first center banner_c5</Display>
                    <Value>b5_c5_b_massanutten</Value>
                  </Option>
                  <Option>
                    <Display>massanutten_header banner_c5</Display>
                    <Value>b5_c5_a_massanutten</Value>
                  </Option>
                  <Option>
                    <Display>massanutten_second center banner_c5</Display>
                    <Value>b5_c5_c_massanutten</Value>
                  </Option>
                  <Option>
                    <Display>mazatlan_first center banner_c5</Display>
                    <Value>b5_c5_b_mazatlan</Value>
                  </Option>
                  <Option>
                    <Display>mazatlan_header banner_c5</Display>
                    <Value>b5_c5_a_mazatlan</Value>
                  </Option>
                  <Option>
                    <Display>mazatlan_second center banner_c5</Display>
                    <Value>b5_c5_c_mazatlan</Value>
                  </Option>
                  <Option>
                    <Display>myrtlebeach_first center banner_c5</Display>
                    <Value>b5_c5_b_myrtlebeach</Value>
                  </Option>
                  <Option>
                    <Display>myrtlebeach_header banner_c5</Display>
                    <Value>b5_c5_a_myrtlebeach</Value>
                  </Option>
                  <Option>
                    <Display>myrtlebeach_second center banner_c5</Display>
                    <Value>b5_c5_c_myrtlebeach</Value>
                  </Option>
                  <Option>
                    <Display>newhampshire_first center banner_c5</Display>
                    <Value>b5_c5_b_newhampshire</Value>
                  </Option>
                  <Option>
                    <Display>newhampshire_header banner_c5</Display>
                    <Value>b5_c5_a_newhampshire</Value>
                  </Option>
                  <Option>
                    <Display>newhampshire_second center banner_c5</Display>
                    <Value>b5_c5_c_newhampshire</Value>
                  </Option>
                  <Option>
                    <Display>nychamptons_first center banner_c5</Display>
                    <Value>b5_c5_b_nychamptons</Value>
                  </Option>
                  <Option>
                    <Display>nychamptons_header banner_c5</Display>
                    <Value>b5_c5_a_nychamptons</Value>
                  </Option>
                  <Option>
                    <Display>nychamptons_second center banner_c5</Display>
                    <Value>b5_c5_c_nychamptons</Value>
                  </Option>
                  <Option>
                    <Display>orlando_first center banner_c5</Display>
                    <Value>b5_c5_b_orlando</Value>
                  </Option>
                  <Option>
                    <Display>orlando_header banner_c5</Display>
                    <Value>b5_c5_a_orlando</Value>
                  </Option>
                  <Option>
                    <Display>orlando_second center banner_c5</Display>
                    <Value>b5_c5_c_orlando</Value>
                  </Option>
                  <Option>
                    <Display>outdoorsparks_first center banner_c5</Display>
                    <Value>b6_c5_a_outdoorsparks</Value>
                  </Option>
                  <Option>
                    <Display>outdoorsparks_second center banner_c5</Display>
                    <Value>b6_c5_b_outdoorsparks</Value>
                  </Option>
                  <Option>
                    <Display>outerbanks_first center banner_c5</Display>
                    <Value>b5_c5_b_outerbanks</Value>
                  </Option>
                  <Option>
                    <Display>outerbanks_header banner_c5</Display>
                    <Value>b5_c5_a_outerbanks</Value>
                  </Option>
                  <Option>
                    <Display>outerbanks_second center banner_c5</Display>
                    <Value>b5_c5_c_outerbanks</Value>
                  </Option>
                  <Option>
                    <Display>palmsprings_first center banner_c5</Display>
                    <Value>b5_c5_b_palmsprings</Value>
                  </Option>
                  <Option>
                    <Display>palmsprings_header banner_c5</Display>
                    <Value>b5_c5_a_palmsprings</Value>
                  </Option>
                  <Option>
                    <Display>palmsprings_second center banner_c5</Display>
                    <Value>b5_c5_c_palmsprings</Value>
                  </Option>
                  <Option>
                    <Display>parkcity_first center banner_c5</Display>
                    <Value>b5_c5_b_parkcity</Value>
                  </Option>
                  <Option>
                    <Display>parkcity_header banner_c5</Display>
                    <Value>b5_c5_a_parkcity</Value>
                  </Option>
                  <Option>
                    <Display>parkcity_second center banner_c5</Display>
                    <Value>b5_c5_c_parkcity</Value>
                  </Option>
                  <Option>
                    <Display>pennsylvaniapoconos_first center banner_c5</Display>
                    <Value>b5_c5_b_pennsylvaniapoconos</Value>
                  </Option>
                  <Option>
                    <Display>pennsylvaniapoconos_header banner_c5</Display>
                    <Value>b5_c5_a_pennsylvaniapoconos</Value>
                  </Option>
                  <Option>
                    <Display>pennsylvaniapoconos_second center banner_c5</Display>
                    <Value>b5_c5_c_pennsylvaniapoconos</Value>
                  </Option>
                  <Option>
                    <Display>phoenixscottsdale_first center banner_c5</Display>
                    <Value>b5_c5_b_phoenixscottsdale</Value>
                  </Option>
                  <Option>
                    <Display>phoenixscottsdale_header banner_c5</Display>
                    <Value>b5_c5_a_phoenixscottsdale</Value>
                  </Option>
                  <Option>
                    <Display>phoenixscottsdale_second center banner_c5</Display>
                    <Value>b5_c5_c_phoenixscottsdale</Value>
                  </Option>
                  <Option>
                    <Display>photography_first center banner_c5</Display>
                    <Value>b6_c5_a_photography</Value>
                  </Option>
                  <Option>
                    <Display>photography_second center banner_c5</Display>
                    <Value>b6_c5_b_photography</Value>
                  </Option>
                  <Option>
                    <Display>platinum_top right banner_c5</Display>
                    <Value>b2_c5_a_platinum</Value>
                  </Option>
                  <Option>
                    <Display>playadelcarmen_first center banner_c5</Display>
                    <Value>b5_c5_b_playadelcarmen</Value>
                  </Option>
                  <Option>
                    <Display>playadelcarmen_header banner_c5</Display>
                    <Value>b5_c5_a_playadelcarmen</Value>
                  </Option>
                  <Option>
                    <Display>playadelcarmen_second center banner_c5</Display>
                    <Value>b5_c5_c_playadelcarmen</Value>
                  </Option>
                  <Option>
                    <Display>postloginhome_lower right banner_c5</Display>
                    <Value>a3_c5_a_postloginhome</Value>
                  </Option>
                  <Option>
                    <Display>scubawatersports_first center banner_c5</Display>
                    <Value>b6_c5_a_scubawatersports</Value>
                  </Option>
                  <Option>
                    <Display>scubawatersports_second center banner_c5</Display>
                    <Value>b6_c5_b_scubawatersports</Value>
                  </Option>
                  <Option>
                    <Display>seasonal_first center banner_c5</Display>
                    <Value>b6_c5_a_seasonal</Value>
                  </Option>
                  <Option>
                    <Display>seasonal_second center banner_c5</Display>
                    <Value>b6_c5_b_seasonal</Value>
                  </Option>
                  <Option>
                    <Display>sedona_first center banner_c5</Display>
                    <Value>b5_c5_b_sedona</Value>
                  </Option>
                  <Option>
                    <Display>sedona_header banner_c5</Display>
                    <Value>b5_c5_a_sedona</Value>
                  </Option>
                  <Option>
                    <Display>sedona_second center banner_c5</Display>
                    <Value>b5_c5_c_sedona</Value>
                  </Option>
                  <Option>
                    <Display>skiing_first center banner_c5</Display>
                    <Value>b6_c5_a_skiing</Value>
                  </Option>
                  <Option>
                    <Display>skiing_second center banner_c5</Display>
                    <Value>b6_c5_b_skiing</Value>
                  </Option>
                  <Option>
                    <Display>smokymountains_first center banner_c5</Display>
                    <Value>b5_c5_b_smokymountains</Value>
                  </Option>
                  <Option>
                    <Display>smokymountains_header banner_c5</Display>
                    <Value>b5_c5_a_smokymountains</Value>
                  </Option>
                  <Option>
                    <Display>smokymountains_second center banner_c5</Display>
                    <Value>b5_c5_c_smokymountains</Value>
                  </Option>
                  <Option>
                    <Display>southernatlanticcoast_first center banner_c5</Display>
                    <Value>b5_c5_b_southernatlanticcoast</Value>
                  </Option>
                  <Option>
                    <Display>southernatlanticcoast_header banner_c5</Display>
                    <Value>b5_c5_a_southernatlanticcoast</Value>
                  </Option>
                  <Option>
                    <Display>southernatlanticcoast_second center banner_c5</Display>
                    <Value>b5_c5_c_southernatlanticcoast</Value>
                  </Option>
                  <Option>
                    <Display>southerncaliforniacoast_first center banner_c5</Display>
                    <Value>b5_c5_b_southerncaliforniacoast</Value>
                  </Option>
                  <Option>
                    <Display>southerncaliforniacoast_header banner_c5</Display>
                    <Value>b5_c5_a_southerncaliforniacoast</Value>
                  </Option>
                  <Option>
                    <Display>southerncaliforniacoast_second center banner_c5</Display>
                    <Value>b5_c5_c_southerncaliforniacoast</Value>
                  </Option>
                  <Option>
                    <Display>spa_first center banner_c5</Display>
                    <Value>b6_c5_a_spa</Value>
                  </Option>
                  <Option>
                    <Display>spa_second center banner_c5</Display>
                    <Value>b6_c5_b_spa</Value>
                  </Option>
                  <Option>
                    <Display>stmartin_first center banner_c5</Display>
                    <Value>b5_c5_b_stmartin</Value>
                  </Option>
                  <Option>
                    <Display>stmartin_header banner_c5</Display>
                    <Value>b5_c5_a_stmartin</Value>
                  </Option>
                  <Option>
                    <Display>stmartin_second center banner_c5</Display>
                    <Value>b5_c5_c_stmartin</Value>
                  </Option>
                  <Option>
                    <Display>tennessee_first center banner_c5</Display>
                    <Value>b5_c5_b_tennessee</Value>
                  </Option>
                  <Option>
                    <Display>tennessee_header banner_c5</Display>
                    <Value>b5_c5_a_tennessee</Value>
                  </Option>
                  <Option>
                    <Display>tennessee_second center banner_c5</Display>
                    <Value>b5_c5_c_tennessee</Value>
                  </Option>
                  <Option>
                    <Display>texasinland_first center banner_c5</Display>
                    <Value>b5_c5_b_texasinland</Value>
                  </Option>
                  <Option>
                    <Display>texasinland_header banner_c5</Display>
                    <Value>b5_c5_a_texasinland</Value>
                  </Option>
                  <Option>
                    <Display>texasinland_second center banner_c5</Display>
                    <Value>b5_c5_c_texasinland</Value>
                  </Option>
                  <Option>
                    <Display>toronto_first center banner_c5</Display>
                    <Value>b5_c5_b_toronto</Value>
                  </Option>
                  <Option>
                    <Display>toronto_header banner_c5</Display>
                    <Value>b5_c5_a_toronto</Value>
                  </Option>
                  <Option>
                    <Display>toronto_second center banner_c5</Display>
                    <Value>b5_c5_c_toronto</Value>
                  </Option>
                  <Option>
                    <Display>vacationideas_large center banner_c5</Display>
                    <Value>a6_c5_a_vacationideas</Value>
                  </Option>
                  <Option>
                    <Display>vallarta_first center banner_c5</Display>
                    <Value>b5_c5_b_vallarta</Value>
                  </Option>
                  <Option>
                    <Display>vallarta_header banner_c5</Display>
                    <Value>b5_c5_a_vallarta</Value>
                  </Option>
                  <Option>
                    <Display>vallarta_second center banner_c5</Display>
                    <Value>b5_c5_c_vallarta</Value>
                  </Option>
                  <Option>
                    <Display>vancouver_first center banner_c5</Display>
                    <Value>b5_c5_b_vancouver</Value>
                  </Option>
                  <Option>
                    <Display>vancouver_header banner_c5</Display>
                    <Value>b5_c5_a_vancouver</Value>
                  </Option>
                  <Option>
                    <Display>vancouver_second center banner_c5</Display>
                    <Value>b5_c5_c_vancouver</Value>
                  </Option>
                  <Option>
                    <Display>vermont_first center banner_c5</Display>
                    <Value>b5_c5_b_vermont</Value>
                  </Option>
                  <Option>
                    <Display>vermont_header banner_c5</Display>
                    <Value>b5_c5_a_vermont</Value>
                  </Option>
                  <Option>
                    <Display>vermont_second center banner_c5</Display>
                    <Value>b5_c5_c_vermont</Value>
                  </Option>
                  <Option>
                    <Display>virginia_first center banner_c5</Display>
                    <Value>b5_c5_b_virginia</Value>
                  </Option>
                  <Option>
                    <Display>virginia_header banner_c5</Display>
                    <Value>b5_c5_a_virginia</Value>
                  </Option>
                  <Option>
                    <Display>virginia_second center banner_c5</Display>
                    <Value>b5_c5_c_virginia</Value>
                  </Option>
                </Datum>
                <Datum ID="E01-D13" Name="Honor Publication Dates" Type="Boolean">false</Datum>
                <Datum ID="E01-D07" Name="Max Results" Type="Number">1</Datum>
                <Datum ID="E01-D08" Name="Score Results" Type="Boolean" Exposed="false">false</Datum>
                <Datum ID="E01-D09" Name="Response Root Node" Type="String" Exposed="false">documents</Datum>
                <Datum ID="E01-D10" Name="Response Param Node" Type="String" Exposed="false">document</Datum>
                <Datum ID="E01-D11" Name="Property Map Path" Type="String" Exposed="false"/>
                <Group ID="E01-G01" Name="Default Rules Values" Replicatable="true" CloneGroupID="hixbduq1">
                  <Datum ID="E01-G01-D01" Name="Rule Name" Type="SelectSingle" Changed="true">
                    <Generator Object="com.rci.livesite.targeting.PropertyMapGenerator" Method="getOptions"/>
                    <Option Selected="true">
                      <Display>Application Type</Display>
                      <Value>Application Type</Value>
                    </Option>
                  </Datum>
                  <Datum ID="E01-G01-D02" Name="Rule Value" Type="String"/>
                </Group>
                <Datum ID="E01-D12" Name="Default Document" Type="DCR" Changed="true">
                  <DCR Category="rci" Type="Offers">templatedata/rci/Offers/data/en_US/5rules-s1/c5s1-so-wvr-contact-phone.xml</DCR>
                </Datum>
              </Parameters>
              <Object Scope="local">com.rci.livesite.targeting.ContentRetriever</Object>
              <Method>getTargetedContent</Method>
            </External>
          </Data>
        </Segment>
      </Segments>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-2:Horizontal Triple Wid</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: c05-s2 --&gt;

 &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/targeted-rules-based/c5-s2-horizontal-triple-wide.xsl"/&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-4:Horizontal Double Wi</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: c05-s6 --&gt;

 &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/targeted-rules-based/c5-s4-v1-horizontal-double-wide.xsl" /&gt; 
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-1: Vertical Short</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: c05-s3 --&gt;

 &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/targeted-rules-based/c5-s1-vertical-short.xsl" /&gt; 
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-5: Horizontal Destinati</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: c05-s7 --&gt;

 &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/targeted-rules-based/c5-s5-horizontal-destination.xsl"/&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-3 : Vertical Tall</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: c05-s8 --&gt;

 &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/targeted-rules-based/c5-s3-v1-vertical-tall.xsl" /&gt; 
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="true" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>Default</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Default XSL --&gt;

  &lt;xsl:include href="http://www.interwoven.com/livesite/xsl/HTMLTemplates.xsl"/&gt;
  &lt;xsl:include href="http://www.interwoven.com/livesite/xsl/StringTemplates.xsl"/&gt;
  &lt;xsl:template match="/"&gt;
    &lt;div&gt;
    &lt;/div&gt;
  &lt;/xsl:template&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
    </Component>
    <Component ID="1574624268876" Version="3.1.1.0" PageID="0" TemplateComponentID="0" CanBeActive="true" Checksum="110ecbce77790f5538bfb7ca35ed9ce1142f6292">
      <Description/>
      <SelectedSkin>S-0: Video Default</SelectedSkin>
      <DisplayName>Video</DisplayName>
      <Name>Video</Name>
      <IsMobileComponent>false</IsMobileComponent>
      <BaseComponent Version="10"><![CDATA[Manual - DCR Browse/Video.component]]></BaseComponent>
      <ContainerProperties ID="0" locked="false">
        <FixedLayoutArea ID="row-2-area-2" index="1"/>
        <CacheTime>-1</CacheTime>
        <BGColor/>
        <Width>200</Width>
        <Height>200</Height>
        <Top>10</Top>
        <Left>10</Left>
        <ZIndex>0</ZIndex>
        <RenderInRuntime>true</RenderInRuntime>
        <JavascriptCallback/>
        <WidthType/>
        <HeightType/>
        <WidthPercent/>
      </ContainerProperties>
      <InternalProperties/>
      <Locks>
        <ContainerProperties locked="false" Changed="false"/>
        <Properties locked="false" Changed="false"/>
        <Data locked="false" Changed="false"/>
      </Locks>
      <Segments>
        <Segment ID="0">
          <Properties ComponentID="1574624268876"/>
          <Data>
            <Datum ID="DCR" Name="VideoDCR" Type="DCR" Changed="true">
              <DCR Category="rci" Type="Video">templatedata/rci/Video/data/en_US/all-inclusive.xml</DCR>
            </Datum>
            <Datum ID="E01-D14" Name="Location" Type="SelectSingle">
              <Option>
                <Display>None</Display>
                <Value/>
              </Option>
              <Option Selected="true">
                <Display>Location1</Display>
                <Value>Location1</Value>
              </Option>
              <Option>
                <Display>Location2</Display>
                <Value>Location2</Value>
              </Option>
            </Datum>
          </Data>
        </Segment>
      </Segments>
      <Stylesheet Default="false" PageType="html5" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-1: Video</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
 &lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
   &lt;!-- Skin: c06-s2 --&gt;

&lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/manual-dcr-browse/c6-s1-video.xsl" /&gt;
 &lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="true" PageType="html5" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-0: Video Default</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
 &lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
   &lt;!-- Skin: c06-s2 --&gt;

   &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/manual-dcr-browse/c6-s0-video.xsl" /&gt;
 &lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
    </Component>
    <Component ID="1574624268877" Version="3.1.1.0" PageID="0" TemplateComponentID="0" CanBeActive="true" Checksum="fe99bba6b048d7bce03d16374dbf8fbc82de8ab6">
      <Description/>
      <SelectedSkin>S-0: Post-Login</SelectedSkin>
      <DisplayName>Share - Print</DisplayName>
      <Name>Share - Print</Name>
      <IsMobileComponent>false</IsMobileComponent>
      <BaseComponent Version="11"><![CDATA[Header - Footer/Share - Print.component]]></BaseComponent>
      <ContainerProperties ID="0" locked="false">
        <FixedLayoutArea index="0" ID="row-2-area-1"/>
        <CacheTime>0</CacheTime>
        <BGColor/>
        <Width>200</Width>
        <Height>200</Height>
        <Top>10</Top>
        <Left>10</Left>
        <ZIndex>0</ZIndex>
        <RenderInRuntime>true</RenderInRuntime>
        <JavascriptCallback/>
        <WidthType/>
        <HeightType/>
        <WidthPercent/>
      </ContainerProperties>
      <InternalProperties/>
      <Locks>
        <ContainerProperties locked="false" Changed="false"/>
        <Properties locked="false" Changed="false"/>
        <Data locked="false" Changed="false"/>
      </Locks>
      <Segments>
        <Segment ID="0">
          <Properties ComponentID="1574624268877"/>
          <Data>
            <Datum ID="DCR" Name="LabelsDCR" Type="DCR" Changed="true">
              <DCR Category="rci" Type="Labels">templatedata/rci/Labels/data/en_US/wvr-club-labels.xml</DCR>
            </Datum>
          </Data>
        </Segment>
      </Segments>
      <Stylesheet Default="true" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S-0: Post-Login</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Default XSL --&gt;

 &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/c10-s0-share-print-post-login.xsl" /&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
      <Stylesheet Default="false" PageType="htmlQuirksMode" RequiredPageLayout="" ContentType="" RenderingEngine="xsl">
        <Name>S1: Pre-Login</Name>
        <XSL>&lt;!DOCTYPE html-entities SYSTEM "http://www.interwoven.com/livesite/xsl/xsl-html.dtd"&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;!-- Skin: Default XSL --&gt;

 &lt;xsl:include href="http://www.interwoven.com/custom/iwov-resources/xsl/header-footer/c10-s1-share-print-pre-login.xsl" /&gt;
&lt;/xsl:stylesheet&gt;</XSL>
      </Stylesheet>
    </Component>
  </Page_Content>
</Page>"""
 
i = 0

for x in titles:
	p = s % (descriptions[i], dcr[i])
	i += 1
	directory = os.path.join("c:\\", 'Users', 'c19306', 'Downloads', 'sotest', 'wvr', x)
	f = open(directory, 'w+')
	f.write(p)
	f.close()