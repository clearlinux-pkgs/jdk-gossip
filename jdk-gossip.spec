#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-gossip
Version  : 2.0.0
Release  : 2
URL      : http://github.com/jdillon/gossip/archive/release-2.0.0.tar.gz
Source0  : http://github.com/jdillon/gossip/archive/release-2.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-gossip-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-hawtjni-project
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jansi
BuildRequires : jdk-jansi-native
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-junit4
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
<!--
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

%package data
Summary: data components for the jdk-gossip package.
Group: Data

%description data
data components for the jdk-gossip package.


%prep
%setup -q -n gossip-release-2.0.0

python3 /usr/share/java-utils/pom_editor.py pom_remove_parent
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  org.codehaus.mojo:animal-sniffer-maven-plugin

%build
python3 /usr/share/java-utils/mvn_build.py -- -Dmaven.javadoc.skip=true

%install
xmvn-install  -R .xmvn-reactor -n gossip -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/gossip/gossip-bootstrap-slf4j.jar
/usr/share/java/gossip/gossip-bootstrap.jar
/usr/share/java/gossip/gossip-core.jar
/usr/share/java/gossip/gossip-extra.jar
/usr/share/java/gossip/gossip-slf4j.jar
/usr/share/java/gossip/gossip-support.jar
/usr/share/maven-metadata/gossip.xml
/usr/share/maven-poms/gossip/gossip-bootstrap-slf4j.pom
/usr/share/maven-poms/gossip/gossip-bootstrap.pom
/usr/share/maven-poms/gossip/gossip-core.pom
/usr/share/maven-poms/gossip/gossip-extra.pom
/usr/share/maven-poms/gossip/gossip-slf4j.pom
/usr/share/maven-poms/gossip/gossip-support.pom
/usr/share/maven-poms/gossip/gossip.pom
