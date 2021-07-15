#include <fstream>
#include <iostream>
using namespace std;


const string python = "python3";

string get_filename();

string get_filter_choice();

int main() {
    cout << "Let's touch up an image!" << endl;
    string filename = get_filename();
    cout << "Using image " << filename << "." << endl;
    string choice = get_filter_choice();
    cout << "Go to you desktop screen to see your image!" << endl;
    string command = python + " ../Filter.py " + filename + choice;
    system(command.c_str());
    return 0;
}


string get_filename(){
    string filename;
    cout << "Enter the filename of an image you'd like to touch up: ";
    cin >> filename;
    ifstream are_you_there;
    are_you_there.open("../" + filename);
    bool exists = bool(are_you_there);
    string extension = filename.substr(filename.find(".") + 1);
    if (extension != "jpg" &&
        extension != "jpeg" &&
        extension != "jpe" &&
        extension != "png" ||
        !exists) {
        filename = "RallyCat.png";
    }
    return filename;
}


string get_filter_choice(){
    char letter_ans;
    string filter_choice;
    cout << "choose a transformation" << endl;
    cout << "(a) change color, (b) blur, (c) sharpen" << endl;
    cin >> letter_ans;
    while(letter_ans != 'a' &&
          letter_ans != 'b' &&
          letter_ans != 'c'){
        cout << "Enter 'a', 'b', or 'c': ";
        cin >> letter_ans;
    }

    if(letter_ans == 'a'){
        cout << "Which color?" << endl;
        cout << "(d) Blue, (e) Red, (f) Green, (g) Orange" << endl;
        cin >> letter_ans;
        while(letter_ans != 'd' &&
              letter_ans != 'e' &&
              letter_ans != 'f' &&
              letter_ans != 'g'){
            cout << "Enter 'd', 'e', 'f', or 'g': ";
            cin >> letter_ans;
        }
    }

    else if(letter_ans == 'b'){
        cout << "Which kind of blur would you like to apply?" << endl;
        cout << "(h) Normal Blur, (i) Gaussian Blur, (j) Median Blur, (k) Bilateral Blur" << endl;
        cin >> letter_ans;
        while(letter_ans != 'h' &&
              letter_ans != 'i' &&
              letter_ans != 'j' &&
              letter_ans != 'k'){
            cout << "Enter 'h', 'i', 'j', or 'k': ";
            cin >> letter_ans;
        }
    }

    if (letter_ans == 'c') {
        filter_choice = " sharpen";
    }
    else if (letter_ans == 'd') {
        filter_choice = " blue";
    }
    else if (letter_ans == 'e') {
        filter_choice = " red";
    }
    else if (letter_ans == 'f') {
        filter_choice = " green";
    }
    else if (letter_ans == 'g') {
        filter_choice = " orange";
    }
    else if (letter_ans == 'h') {
        filter_choice = " blur";
    }
    else if (letter_ans == 'i') {
        filter_choice = " gaussianBlur";
    }
    else if (letter_ans == 'j') {
        filter_choice = " medianBlur";
    }
    else if (letter_ans == 'k') {
        filter_choice = " bilateralBlur";
    }
    return filter_choice;
}
