# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define section free

Name:           kxml2
Version:        2.2.2
Release:        2.0.4
Epoch:          0
Summary:        Small XML pull parser specially designed for constrained environments
License:        BSD
URL:            http://kxml.sourceforge.net/
Group:          Development/Java
Source0:        http://dl.sourceforge.net/sourceforge/kxml/kxml2-src-2.2.2.zip
Source1:        http://repo1.maven.org/maven2/net/sf/kxml/kxml2/2.2.2/kxml2-2.2.2.pom
BuildRequires:  jpackage-utils >= 0:1.7.4
BuildRequires:  java-devel = 0:1.5.0
BuildRequires:  java-rpmbuild
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  xpp3 >= 0:1.1.3.1
Requires:  java >= 0:1.5.0
Requires:  xpp3
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires(post):   jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
kXML 2 is a small XML pull parser, specially designed for constrained
environments such as Applets, Personal Java or MIDP devices. In contrast
to kXML 1, kXML 2 is based on the common XML pull API. The 1.x version
of kXML will stay available at kxml.enhydra.org.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%remove_java_binaries
ln -sf $(build-classpath xpp3) lib/xmlpull_1_1_3_1.jar

%build
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap net.sf.kxml %{name} %{version} JPP %{name}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}.pom

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/%{name}-min-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-min-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -p -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr www/kxml2/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(0644,root,root,0755)
%{_javadir}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}

%files javadoc
%defattr(0644,root,root,0755)
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%dir %{_javadocdir}/%{name}



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.2.2-2.0.3mdv2011.0
+ Revision: 620044
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0:2.2.2-2.0.2mdv2010.0
+ Revision: 429698
- rebuild

* Thu Jul 10 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:2.2.2-2.0.1mdv2009.0
+ Revision: 233587
- import kxml2


