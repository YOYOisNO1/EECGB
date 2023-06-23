def program3791():
    #include <iostream>
    
    using namespace std;
    
    int main(){
        // take inputs
        long long board_length;
        long long price_coordinate_x;
        long long price_coordinate_y;
    
        cin >> board_length;
        cin >> price_coordinate_x;
        cin >> price_coordinate_y;
        
        // starting points for kings
        int white_x = 1;
        int white_y = 1;
        long long black_x = board_length;
        long long black_y = board_length;
    
        // Difference between price coordinate points
        long long point_difference_white = llabs(price_coordinate_x-price_coordinate_y); 
        long long point_difference_black = llabs(price_coordinate_x-price_coordinate_y);
        
        // if x > y => y will be the first value we'll reach
        if (price_coordinate_x > price_coordinate_y) {
            point_difference_white += llabs(white_x-price_coordinate_y);
            point_difference_black += llabs(black_x-price_coordinate_x); 
        }
        else if (price_coordinate_x < price_coordinate_y) {
            point_difference_white += llabs(white_x-price_coordinate_x);
            point_difference_black += llabs(black_y-price_coordinate_y);
        }
        else {
            point_difference_white += llabs(white_x-price_coordinate_x);
            point_difference_black += llabs(black_x-price_coordinate_x);
        }
        
        if (point_difference_black >= point_difference_white) {
            cout << "White" << endl;
        }
        else if (point_difference_black < point_difference_white) {
            cout << "Black" << endl;
        }
        return 0;
    }