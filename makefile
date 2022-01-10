EXECUTABLE = fm_transmitter
VERSION = 0.9.5
FLAGS = -Wall -O3 -std=c++11
TRANSMITTER = -fno-strict-aliasing -I/opt/vc/include
ifeq ($(GPIO21), 1)
	TRANSMITTER += -DGPIO21
endif

all: fm_transmitter.o mailbox.o sample.o wave_reader.o transmitter.o
	g++ -L/opt/vc/lib -o $(EXECUTABLE) fm_transmitter.o mailbox.o sample.o wave_reader.o transmitter.o -lm -lpthread -lbcm_host

mailbox.o: mailbox.c mailbox.h
	g++ $(FLAGS) -c mailbox.c

sample.o: sample.cpp sample.hpp
	g++ $(FLAGS) -c sample.cpp

wave_reader.o: wave_reader.cpp wave_reader.hpp
	g++ $(FLAGS) -c wave_reader.cpp

transmitter.o: transmitter.cpp transmitter.hpp
	g++ $(FLAGS) $(TRANSMITTER) -c transmitter.cpp

fm_transmitter.o: fm_transmitter.cpp
	g++ $(FLAGS) -DVERSION=\"$(VERSION)\" -DEXECUTABLE=\"$(EXECUTABLE)\" -c fm_transmitter.cpp

clean:
	rm *.o
