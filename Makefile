all:
	echo "nothing to compile."

install-config:
	cp -r etc/ /

install-init:
	cp -r init/ /etc/site-init
	cp xinit /etc/init.d/
	ln -sf /etc/init.d/xinit /etc/rc2.d/S99-xinit

install-tools:
	install -m755 rfconn /usr/bin/
	install -m755 display-stats.py /usr/bin/
	install -m755 sethost /usr/bin/
	install -m755 aptconf /usr/bin/
	install -m755 wifisetup /usr/bin/
	install -m755 nanopi-downloader /usr/bin/
