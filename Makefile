all: report clean

report:
	pdflatex -interaction batchmode rapport.tex
	pdflatex -interaction batchmode rapport.tex

verbose:
	pdflatex rapport.tex
	pdflatex rapport.tex

test:
	@printf "==== TESTS PART 1 ====\n"
	@python3 src/test1.py
	@printf "\n==== TESTS PART 2 ====\n"
	@python3 src/test2.py
	@printf "\n==== TESTS PART 3 ====\n"
	@python3 src/test3.py
	@printf "\n==== TESTS PART 4 ====\n"
	@python3 src/test4.py

clean:
	rm -rf *.log *.aux *.toc