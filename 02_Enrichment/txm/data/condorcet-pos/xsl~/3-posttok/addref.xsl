<?xml version="1.0"?>
<xsl:stylesheet xmlns:edate="http://exslt.org/dates-and-times"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="tei edate" version="2.0">

  <xsl:output method="xml" encoding="utf-8" omit-xml-declaration="no"/>

  <xsl:template match="*">
    <xsl:choose>
      <xsl:when test="namespace-uri()=''">
        <xsl:element namespace="http://www.tei-c.org/ns/1.0" name="{local-name(.)}">
          <xsl:apply-templates select="*|@*|processing-instruction()|comment()|text()"/>
        </xsl:element>
      </xsl:when>
      <xsl:otherwise>
        <xsl:copy>
          <xsl:apply-templates select="*|@*|processing-instruction()|comment()|text()"/>
        </xsl:copy>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="@*|processing-instruction()|comment()">
    <xsl:copy/>
  </xsl:template>


  <xsl:template match="text()">
    <xsl:value-of select="."/>
  </xsl:template>
	
	
	<xsl:template match="tei:w">
	  <xsl:variable name="textID">
	    <xsl:choose>
	      <xsl:when test="ancestor::tei:text[@idbfm]">
	        <xsl:value-of select="ancestor::tei:text/@idbfm"/>
	      </xsl:when>	      
	      <xsl:when test="ancestor::tei:text[@*[local-name()='id']]">
	        <xsl:value-of select="ancestor::tei:text/@*[local-name()='id'][1]"/>
	      </xsl:when>
	      <xsl:otherwise>
	      	<xsl:analyze-string select="document-uri(/)" regex="^(.*)/([^/]+)\.([^.]+)$">
	      		<xsl:matching-substring>
	      			<xsl:value-of select="regex-group(2)"/>
	      		</xsl:matching-substring>
	      	</xsl:analyze-string>	     
	      </xsl:otherwise>
	    </xsl:choose>
	  </xsl:variable>	  
			<xsl:variable name="pbN">
				<xsl:choose>
					<xsl:when test="preceding::tei:pb[1][@n]">
						<xsl:value-of select="preceding::tei:pb[1]/@n"/>
					</xsl:when>
					<xsl:otherwise>NN</xsl:otherwise>
				</xsl:choose>
			</xsl:variable>			
	  <xsl:variable name="lbN">
	    <xsl:choose>
	      <xsl:when test="preceding::tei:lb[1][@n]">
	        <xsl:value-of select="preceding::tei:lb[1]/@n"/>
	      </xsl:when>
	      <xsl:otherwise>NN</xsl:otherwise>
	    </xsl:choose>
	  </xsl:variable>			
		<xsl:copy>
			<xsl:apply-templates select="@*"/>
			<xsl:attribute name="ref">
			  <xsl:value-of select="$textID"/>
				<xsl:if test="not($pbN='NN')">
					<xsl:value-of select="concat(', p. ',$pbN)"/>
				</xsl:if>
				<xsl:if test="not($lbN='NN')">
					<xsl:value-of select="concat(', l. ',$lbN)"/>
				</xsl:if>
			</xsl:attribute>
<!--			<xsl:attribute name="id">
				<xsl:value-of select="concat(ancestor::tei:text/@id,'_',count(preceding::tei:w)+1)"/>
			</xsl:attribute>-->
			<xsl:apply-templates/>
		</xsl:copy>
	</xsl:template>

</xsl:stylesheet>
