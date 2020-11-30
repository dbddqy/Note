//
// Created by yue on 07.09.20.
//

#include <iostream>
#include <thread>

void thread(int num) {
    for (int i = 0; i < num; ++i)
        std::cout << "in thread " << std::this_thread::get_id() << std::endl;
}

int main(int argc, char** argv) {
    std::thread t1(thread, 100);
    std::thread t2(thread, 100);
    std::cout << t1.joinable() << std::endl;
    std::cout << t2.joinable() << std::endl;
    t1.detach();  // doesn't control the thread anymore, let it run in background
    t2.join();  // complete the thread in main thread
    // after detach() or join() thread becomes not joinable
    std::cout << t1.joinable() << std::endl;
    std::cout << t2.joinable() << std::endl;
    std::cout<<"Exit of Main function"<<std::endl;
    return 0;
}
