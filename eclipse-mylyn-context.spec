%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
#  http://download.eclipse.org/mylyn/archive/3.5.1/v20110422-0200/
%global qualifier           v20110422-0200

# Builds the following upstream features:
# - org.eclipse.mylyn.team-feature
# - org.eclipse.mylyn.cdt-feature
# - org.eclipse.mylyn.java-feature
# - org.eclipse.mylyn.pde-feature
# - org.eclipse.mylyn.context-feature

Name: eclipse-mylyn-context
Summary: Eclipse Mylyn context specific features
Version: 3.5.1
Release: 1
License: EPL
URL: http://www.eclipse.org/mylyn

# bash fetch-eclipse-mylyn-context.sh
Source0: eclipse-mylyn-context-R_3_5_1-fetched-src.tar.bz2
Source1: fetch-eclipse-mylyn-context.sh

BuildArch: noarch

BuildRequires: java-devel >= 1.5.0
BuildRequires: eclipse-platform >= 0:3.4.0
BuildRequires: eclipse-pde >= 0:3.4.0
BuildRequires: eclipse-jdt >= 0:3.4.0
BuildRequires: eclipse-cdt
BuildRequires: eclipse-mylyn >= 3.5.0


# eclipse-mylyn-context

Requires: eclipse-platform >= 0:3.4.0
Requires: eclipse-mylyn >= 3.5.0
Group: Development/Java

%description
Provides the Eclipse Mylyn Task-Focused Interface.


# eclipse-mylyn-context-java

%package java
Summary:  Mylyn Bridge:  Java Development
Requires: eclipse-jdt
Requires: %{name} = %{version}-%{release}
Provides: eclipse-mylyn-java = %{version}-%{release}
Obsoletes: eclipse-mylyn-java < %{version}-%{release}
Group: Development/Java

%description java
Mylyn Task-Focused UI extensions for JDT.  Provides focusing of Java
element views and editors.


# eclipse-mylyn-context-pde

%package pde
Summary:  Mylyn Bridge:  Plug-in Development
Requires: eclipse-pde
Requires: %{name}-java = %{version}-%{release}
Provides: eclipse-mylyn-pde = %{version}-%{release}
Obsoletes: eclipse-mylyn-pde < %{version}-%{release}
Group: Development/Java

%description pde
Mylyn Task-Focused UI extensions for PDE, Ant, Team Support and CVS.


# eclipse-mylyn-context-cdt

%package cdt
Summary:  Mylyn Bridge:  C/C++ Development
Requires: %{name} = %{version}-%{release}
Requires: eclipse-cdt
Group: Development/Java
Provides: eclipse-cdt-mylyn = 2:1.0.0-1.fc12
Provides: eclipse-mylyn-cdt = %{version}-%{release}
Obsoletes: eclipse-mylyn-cdt < %{version}-%{release}
Obsoletes: eclipse-cdt-mylyn < 2:1.0.0

%description cdt
Mylyn Task-Focused UI extensions for CDT.  Provides focusing of C/C++
element views and editors.


# eclipse-mylyn-context-team

%package team
Summary:  Mylyn Context Connector: Team Support
Requires: %{name} = %{version}-%{release}
Group: Development/Java

%description team
Mylyn Task-Focused UI extensions for Team version control.


%prep
%setup -q -n org.eclipse.mylyn.contexts


%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.context_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar -d "mylyn"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.team_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.java_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar -d "jdt"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.pde_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar -d "sdk jdt"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.cdt.mylyn \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar -d "cdt"


%install
install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/mylyn-context
install -d -m 755 %{buildroot}%{install_loc}/mylyn-context-team
install -d -m 755 %{buildroot}%{install_loc}/mylyn-java
install -d -m 755 %{buildroot}%{install_loc}/mylyn-pde
install -d -m 755 %{buildroot}%{install_loc}/mylyn-cdt

unzip -q -o -d %{buildroot}%{install_loc}/mylyn-context \
 build/rpmBuild/org.eclipse.mylyn.context_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-context-team \
 build/rpmBuild/org.eclipse.mylyn.team_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-java \
 build/rpmBuild/org.eclipse.mylyn.java_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-pde \
 build/rpmBuild/org.eclipse.mylyn.pde_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-cdt \
 build/rpmBuild/org.eclipse.cdt.mylyn.zip


# eclipse-mylyn-context

%files
%defattr(-,root,root,-)
%{install_loc}/mylyn-context
%doc org.eclipse.mylyn.context-feature/license.html
%doc org.eclipse.mylyn.context-feature/epl-v10.html


# eclipse-mylyn-context-java

%files java
%defattr(-,root,root,-)
%{install_loc}/mylyn-java
%doc org.eclipse.mylyn.java-feature/license.html
%doc org.eclipse.mylyn.java-feature/epl-v10.html


# eclipse-mylyn-context-pde

%files pde
%defattr(-,root,root,-)
%{install_loc}/mylyn-pde
%doc org.eclipse.mylyn.pde-feature/license.html
%doc org.eclipse.mylyn.pde-feature/epl-v10.html


# eclipse-mylyn-context-cdt

%files cdt
%defattr(-,root,root,-)
%{install_loc}/mylyn-cdt
%doc org.eclipse.mylyn.cdt-feature/license.html
%doc org.eclipse.mylyn.cdt-feature/epl-v10.html


# eclipse-mylyn-context-team

%files team
%defattr(-,root,root,-)
%{install_loc}/mylyn-context-team
%doc org.eclipse.mylyn.team-feature/license.html
%doc org.eclipse.mylyn.team-feature/epl-v10.html


