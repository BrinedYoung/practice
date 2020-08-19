CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR= ./include/

#SRCS=$(SRCDIR)Monte_Carlo_simulation.c \ 
#	$(SRCDIR)stat.c 

SRCS=$(wildcard $(SRCDIR)*.c)

# non-path filename
filename=$(notdir $(SRCS))

# the obj target of a source code using the pattern rule
OBJS=$(patsubst %.c,$(OBJDIR)%.o,$(filename))

all:soucestat
	./bin/soucestat
    
soucestat: $(OBJS)  
	$(CC) -o $(BINDIR)$@ $(OBJS) 

$(OBJS):$(SRCS)
	$(CC) -o $@ -c $(SRCDIR)$(patsubst  %.o,%.c,$(notdir $@))  -I$(INCDIR)

clean:
	 del .\obj\stat.o
	 del .\obj\Monte_Carlo_simulation.o