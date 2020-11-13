#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <fstream>
#include <numeric>
#define p_num_1 8
#define p_num_2 3

using namespace std;

int judge(int x) {
    int a=0;
    if(x == 3 |x == 5|x == 7 |x == 8 |x ==13|x == 14)
      a= 1;
    return a;
}



int main(){
  std::string name,title,num;

  std::ifstream in("exam.txt");
  std::cin.rdbuf(in.rdbuf());

  vector<vector<vector<int>>> score(16, vector<vector<int>>(10, vector<int>(p_num_1+p_num_2)));
  
  
  

for(int examinee=0;examinee<p_num_1;examinee++){
  cin >> name;
  //cout <<"\n"<< name << "\n";
    for(int music_id=0;music_id<16;music_id++){
        cin >> title;
        //cout <<"\n" << title<<"\n";
        for(int adjective=0;adjective<10;adjective++){
          cin >> num;
          num.erase(0,2);
          //cout <<" "<< num;

          try{
          score.at(music_id).at(adjective).at(examinee)=stoi(num);
          }
          catch(const std::invalid_argument& e){
            cout << "invalid argument" << endl;
          }
          catch(const std::out_of_range& e){
            cout << "Out of range" <<endl;
          }

        }
    }
}

for(int examinee=p_num_1;examinee<p_num_1+p_num_2;examinee++){
  cin >> name;
  //cout <<"\n"<< name << "\n";
  for(int adjective=0;adjective<10;adjective++){
        cin >> title;
        //cout <<"\n" << title<<"\n";
        for(int music_id=0;music_id<16;music_id++){
          cin >> num;
          if(music_id==0){
            num.erase(0,1);
          }
          num.erase(1);
          //cout <<" "<< num;
          try{
          score.at(music_id).at(adjective).at(examinee)=stoi(num);
          }
          catch(const std::invalid_argument& e){
            cout << "invalid argument" << endl;
          }
          catch(const std::out_of_range& e){
            cout << "Out of range" <<endl;
          }

        } 
    }
}

in.close();
float sum;
ofstream ofs("test.csv");  // ファイルパスを指定する
//ofstream ofs2("test2.csv");

int x;

ofs<<"曲,予想カテゴリ,被験者,快適な/不快な,明るい/暗い,滑らか/ざらついた,鋭い/鈍い,騒々しい/静かな,硬い/柔らかい,高い/低い,澄んだ/濁った,弱い/強い,変動の大きい/小さい"<<endl;;

for(int music_id=0;music_id<16;music_id++){
   x = judge(music_id);
     for(int examinee=0;examinee<p_num_1+p_num_2;examinee++){
        ofs << music_id << ",";
    if(x == 0)
        ofs << "普通" << ",";
    else if (x== 1)
        ofs << "不快な" << ",";
        
        ofs << examinee << ",";
          for(int adjective=0;adjective<10;adjective++){
              ofs << score.at(music_id).at(adjective).at(examinee)<<",";
          }
        ofs <<endl;
        }
  }


ofs.close();







/*
for(int music_id=0;music_id<16;music_id++){
          //ofs<<"music:"<< music_id <<endl;;


  for(int adjective=0;adjective<10;adjective++){
         // ofs<<"adj:"<< char(65+adjective) <<endl;;

          

          for(int examinee=0;examinee<p_num_1+p_num_2;examinee++){
            ofs << score.at(music_id).at(adjective).at(examinee)<<",";
          }
          //ofs<<",";
          sum = std::accumulate(score.at(music_id).at(adjective).begin(),score.at(music_id).at(adjective).end(), 0);
          //ofs2 << sum/(p_num_1+p_num_2)<<",";

          ofs <<endl;
        }
          //ofs2 <<endl;
          ofs <<endl;
  }
*/




/*
for(int music_id=0;music_id<16;music_id++){
          cout <<"\n"<<"music:"<< music_id << " ";
  for(int adjective=0;adjective<10;adjective++){
          cout << char(65+adjective);
          sum = std::accumulate(score.at(music_id).at(adjective).begin(),score.at(music_id).at(adjective).end(), 0);
          cout << sum/p_num_1+p_num_2<< " ";
          
        }
  }
*/

}
