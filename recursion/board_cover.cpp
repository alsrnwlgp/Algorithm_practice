#include <vector>
#include <iostream>
#include <string>

using namespace std;

const int coverType[4][3][2] = {
	{{0,0}, {0,1}, {1,0}},
	{{0,0}, {1,0}, {1,-1}},
	{{0,0}, {1,0}, {1,1}},
	{{0,0}, {0,1}, {1,1}}
};

bool set_block(vector<vector<int>>& board, int y, int x, int type, int delta){
	bool ok = true;
	for(int i=0; i<3; i++){
		const int ny = y + coverType[type][i][0];
		const int nx = x + coverType[type][i][1];
		if(ny < 0 || ny >= board.size() || nx < 0 || nx >= board[0].size())
			ok = false;
		else if((board[ny][nx] += delta) > 1)
			ok = false;
	}
	return ok;
}

int cover(vector<vector<int>>& board){
	int y = -1, x = -1;
	for(int i = 0; i < board.size(); i++){
		for(int j = 0; j < board[i].size(); j++){
			if(board[i][j] == 0){
				y=i;
				x=j;
				break;
			}
		}
		if(y!=-1) break; //이게 굳이 필요한가?
	}
	//기저사례
	if(y==-1) return 1;
	int ret = 0;
	for(int type=0; type<4; type++){
		if(set_block(board,y,x,type,1))
		  ret += cover(board);
		set_block(board,y,x,type,-1);
	}
	return ret;
}

int height, width;
	

int main(void)

{

        int test_case, H, W; //H=height, W=width

        vector<vector<int>> board;

        char bw[20]; //black/white

 

        cin >> test_case;

        if (test_case < 0 || test_case > 30)

               exit(-1);

 

        for (int i = 0; i < test_case; i++)

        {

               cin >> H >> W;

               if (H < 1 || H>20 || W < 1 || W>20)

                       exit(-1);

               for (int i = 0; i < H; i++)

               {

                       cin >> bw;

                       for (int j = 0; j < W; j++)

                              board[i][j] = (bw[j] == '#') ? 1 : 0;

               }

               cout << cover(board) << endl;

        }

        return 0;

}