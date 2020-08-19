SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: dllstat
	./bin/dllstat

dllstat: statobj  
	gcc -o $(BINDIR)dllstat $(OBJDIR)stat.o -L$(BINDIR) -lsimulation
#	gcc -o $(BINDIR)statApp $(OBJDIR)statApp.o -L$(BINDIR) -lstat -Wl,-rpath=./bin/  

statobj: $(SRCDIR)stat.c 
	gcc -c -o $(OBJDIR)stat.o $(SRCDIR)stat.c -I$(INCDIR)

clean:
	 del .\obj\stat.o