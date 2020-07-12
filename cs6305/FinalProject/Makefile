PLAT = linux
CPP = g++
MPICXX = mpicxx

LAPACK_LIB   = 
BLAS_LIB     = 


CPP_WARNINGS = -Wall -ansi
CPP_DEBUG    = -g
CPP_OPTIM    = -O

CPP_FLAGS    = -std=c++11 $(CPP_DEBUG) -D$(PLAT)  $(CPP_WARNINGS)  -lgfortran

ALL_LIBS     = $(LAPACK_LIB) $(BLAS_LIB)  -lgfortran

DEPS = 

##----------------------------------------


main: main.o
	$(CPP) $(CPP_FLAGS) -o main main.o $(ALL_LIBS)


%.o: %.cc %.h $(DEPS)
	$(CPP) $(CPP_FLAGS) -c $<



.PHONY: clean
clean:
	rm -f *~ *.o core main












