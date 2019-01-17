<?xml version="1.0"?>
<xsl:stylesheet xmlns:edate="http://exslt.org/dates-and-times"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="tei edate" version="2.0">

  <xsl:output method="xml" encoding="utf-8" omit-xml-declaration="no"/>


  <xsl:template match="node()|@*">
    <!-- Copy the current node -->
    <xsl:copy>
      <!-- Including any attributes it has and any child nodes -->
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
  
  <xsl:variable name="current-file-name">
    <xsl:analyze-string select="document-uri(.)" regex="^(.*)/([^/]+)\.[^/]+$">
      <xsl:matching-substring>
        <xsl:value-of select="regex-group(2)"/>
      </xsl:matching-substring>
    </xsl:analyze-string>
  </xsl:variable>
 
  
  
<xsl:template match="tei:w">
  <xsl:copy>
    <xsl:apply-templates select="@*"/>
    <xsl:attribute name="xml:id">
      <xsl:text>w_</xsl:text>
      <xsl:value-of select="$current-file-name"/>
      <xsl:text>_</xsl:text>
      <xsl:number level="any"/>
    </xsl:attribute>
    <xsl:apply-templates></xsl:apply-templates>
  </xsl:copy>
</xsl:template>

<xsl:template match="tei:w/@xml:id">
  <xsl:attribute name="oldId"><xsl:value-of select="."/></xsl:attribute>
</xsl:template>

</xsl:stylesheet>
