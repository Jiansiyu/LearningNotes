// ConsoleApplication1.cpp//

#include <math.h>
#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <unistd.h>
#include<random>
#include<string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <iostream>
//#include <armadillo>
//#include <mpi.h>


using namespace std;
//using namespace arma;

int L=40;


double GEN()
{
  static std::default_random_engine e(time(nullptr)+getpid());
  static std::uniform_real_distribution<double> u(0.0,1.0);
  return u(e);
}
inline int mod(int x, int m) {
	if (x >= 0 && x < m)
		return x;
	else if (x < 0)
		return m - 1 - mod(-1 - x, m);
	else
		return x % m;
}

int update(int i,int j,int LAT[L][L],double TEMP)
{
  double deltaE=0;

  deltaE=(2.0)*(LAT[i][mod(j+1,L)]+LAT[i][mod(j-1,L)]+LAT[mod(i+1,L)][j]+LAT[mod(i-1,L)][j])*LAT[i][j];
  //cout<<deltaE<<endl;
  double r=GEN();
  if(r<exp(-deltaE/TEMP))
    {
      LAT[i][j]=-LAT[i][j];
      return 1;
    }
  else
    {
      return 0;
    }
}

void Metropolis(int LAT[L][L],double TEMP)
{
  for(int i=0;i<L;i++)
    {
      for(int j=0;j<L;j++)
	{
	  update(i,j,LAT,TEMP);
	}
    }
}
void MonteCarlo(int steps,int LAT[L][L],double TEMP)
{
  for(int c=0;c<steps;c++)
    {
      Metropolis(LAT,TEMP);
    }
}

void init(int LAT[L][L])
{
  double r=0;
  for(int i=0;i<L;i++)
    {
      for(int j=0;j<L;j++)
	{
	  r=GEN(); 
	  if(r<0.5)
	    {
	      LAT[i][j]=-1;
	    }
	  else
	    {
	      LAT[i][j]=1;
	    }
	}
    }
}

int sum(int LAT[L][L])
{
  double s=0;
  for(int i=0;i<L;i++)
    {
      for(int j=0;j<L;j++)
	{
	  s+=LAT[i][j];
	}
    }
  return s;
}


void GenerateSingleTDataSet(double T, std::string DataFolder="result"){
		int LAT[L][L]={0};
		char Pathname[300];
		sprintf(Pathname,"%s/Grid%d",DataFolder.c_str(),L);
		if (mkdir(Pathname, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH) == -1)
			{
    		if( errno == EEXIST ) {
       	// alredy exists
    			} else {
       			// something else
        		std::cout << "cannot create sessionnamefolder error:" << strerror(errno) << std::endl;
        		throw std::runtime_exception( strerror(errno) );
    			}
		//Generate file and save the data into the file 
		char filename[300];//=std::format("%s/T%0.2f.txt",Pathname,T);
sprintf(filename,"%s/T%0.2f.txt",Pathname,T);
		// generate the Data

		ofstream fout;
      if(T<2.26)
	{ 
	  fout.open(filename,ios_base::out);
	  init(LAT);
	  MonteCarlo(1000,LAT,T);
	  for(int count=0;count<10000;count++)
	    {
	      MonteCarlo(100,LAT,T);
              for(int i=0;i<L;i++)
		{
		  for(int j=0;j<L;j++)
		    {
		      fout<<LAT[i][j];
					if (i*40+j < L*L-1){
							fout<<'\t';
					}else{
						fout<<'\n';
					}
		    }
		}
		if(count%100==0)
	std::cout<<"Current working on:"<<(double)count/10000.0<<std::flush;
	    }
	  fout.close();
	}
      else
	{
	  fout.open(filename,ios_base::out);
	  init(LAT);
	  MonteCarlo(1000,LAT,T);
	  for(int count=0;count<10000;count++)
	    {
	      MonteCarlo(100,LAT,T);
              for(int i=0;i<L;i++)
		{
		  for(int j=0;j<L;j++)
		    {
		      fout<<LAT[i][j];
					if (i*40+j < L*L-1){
							fout<<'\t';
					}else{
						fout<<'\n';
					}
		    }
		}
			if(count%100==0)
			std::cout<<"Current working on:"<<(double)count/10000.0<<std::flush;
	    }
	  fout.close();
	}

}


}

int main (int argc, char **argv){
	L=30;
	for(double T=0.25;T<=4.1;T+=0.25){
		GenerateSingleTDataSet(T);
	}
}

/*
int main(int argc, char **argv)
{
  int LAT[L][L]={0};

  cout<<sum(LAT)<<endl;
  char filename[100];
  ofstream fout;
  //fout.open("test.txt",ios_base::out);
  for(double T=0.25;T<=4.1;T+=0.25)
    {
      if(T<2.26)
	{
          sprintf(filename,"result/T%.2f.txt",T);
	  fout.open(filename,ios_base::out);
	  init(LAT);
	  MonteCarlo(1000,LAT,T);
	  for(int count=0;count<10000;count++)
	    {
	      MonteCarlo(100,LAT,T);
              for(int i=0;i<L;i++)
		{
		  for(int j=0;j<L;j++)
		    {
		      fout<<LAT[i][j]<<'\t';
		    }
		}
	      fout<<'\n';
	    }
	  fout.close();
	}
      else
	{
          sprintf(filename,"result/T%.2f.txt",T);
	  fout.open(filename,ios_base::out);
	  init(LAT);
	  MonteCarlo(1000,LAT,T);
	  for(int count=0;count<10000;count++)
	    {
	      MonteCarlo(100,LAT,T);
              for(int i=0;i<L;i++)
		{
		  for(int j=0;j<L;j++)
		    {
		      fout<<LAT[i][j]<<'\t';
		    }
		}
	      fout<<'\n';
	    }
	  fout.close();
	}
    }


  return 0;
}
*/
