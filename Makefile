compile:
	@cp ./CV/resume.pdf ./files/CV_ShihanLin.pdf
	@python compile.py

install: compile
	@tar -zcf src.tar.gz *.html css/ js/ files/ img/  
	@scp src.tar.gz home:~/homepage/
	@ssh home "bash ~/homepage/install.sh"



