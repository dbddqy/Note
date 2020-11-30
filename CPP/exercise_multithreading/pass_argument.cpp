//
// Created by yue on 07.09.20.
//

#include <iostream>
#include <thread>

void thread(int count, int & num) {
    for (int i = 0; i < count; ++i) {
        num += 1;
//        std::cout << "in thread " << std::this_thread::get_id();
//        std::cout << " num = " << num << std::endl;
    }
}

int num = 0;

int main(int argc, char** argv) {
    for (int i = 0; i < 1000; ++i) {
        num = 0;
        std::thread t1(thread, 2000, std::ref(num));
        std::thread t2(thread, 2000, std::ref(num));
        t1.join();
        t2.join();
        // different threads wants to change the same variable, error might occur
        if (num != 4000)
            std::cout << "error at count = " << i << " num = " << num << std::endl;
    }
    std::cout<<"Exit of Main function"<<std::endl;
    return 0;
}
