ARCH = $(shell uname -i)
ifeq "$(ARCH)" "x86_64"
	# In case of 64 bit system, use these lines
	LIBDIR=/usr/lib64
else 
ifeq "$(ARCH)" "i686"
	# In case of 32 bit system, use these lines
	LIBDIR=/usr/lib
else
ifeq "$(ARCH)" "i386"
	# In case of 32 bit system, use these lines
	LIBDIR=/usr/lib
endif
endif
endif
# Installation directories.
PREFIX  ?= $(DESTDIR)/usr
SBINDIR ?= $(DESTDIR)/sbin
INITDIR ?= $(DESTDIR)/etc/rc.d/init.d

PROG_SRC=mcstrans.c  mcscolor.c  mcstransd.c  mls_level.c
PROG_OBJS= $(patsubst %.c,%.o,$(PROG_SRC))
PROG=mcstransd
INITSCRIPT=mcstrans
CFLAGS ?= -Wall -W -Wundef -Wmissing-noreturn -Wmissing-format-attribute
override CFLAGS += -I../include -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64

all: $(PROG)

$(PROG): $(PROG_OBJS)
	$(CC) $(LDFLAGS) -pie -o $@ $^ -lselinux -lcap -lpcre $(LIBDIR)/libsepol.a

%.o:  %.c 
	$(CC) $(CFLAGS) -fPIE -c -o $@ $<

install: all
	test -d $(SBINDIR) || install -m 755 -d $(SBINDIR)
	install -m 755 $(PROG) $(SBINDIR)
	test -d $(INITDIR) || install -m 755 -d $(INITDIR)
	install -m 755 $(INITSCRIPT).init $(INITDIR)/$(INITSCRIPT)

clean: 
	-rm -f $(OBJS) $(LOBJS) $(TARGET) $(PROG) $(PROG_OBJS) *~ \#*

