# Installation directories.
PREFIX ?= $(DESTDIR)/usr
INCLUDEDIR ?= $(PREFIX)/include
SBINDIR ?= $(PREFIX)/sbin
MANDIR = $(PREFIX)/share/man
LIBDIR ?= $(PREFIX)/lib
BASHCOMPLETIONDIR ?= $(DESTDIR)/etc/bash_completion.d/

CFLAGS ?= -Werror -Wall -W
override CFLAGS += -I$(INCLUDEDIR)
LDLIBS = -lsepol -lselinux -lsemanage -L$(LIBDIR)
SETSEBOOL_OBJS = setsebool.o

BASHCOMPLETIONS=setsebool-bash-completion.sh 

all: setsebool

setsebool: $(SETSEBOOL_OBJS)

install: all
	-mkdir -p $(SBINDIR)
	install -m 755 setsebool $(SBINDIR)
	-mkdir -p $(MANDIR)/man8
	install -m 644 setsebool.8 $(MANDIR)/man8/
	-mkdir -p $(BASHCOMPLETIONDIR)
	install -m 644 $(BASHCOMPLETIONS) $(BASHCOMPLETIONDIR)

relabel:

clean:
	-rm -f setsebool *.o

indent:
	../../scripts/Lindent $(wildcard *.[ch])

