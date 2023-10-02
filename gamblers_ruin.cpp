#include <random>
#include <utility>
#include <random>
#include <cmath>
#include <iostream>
#include <numeric>
#include <algorithm>

std::pair<int,int> gamblers_ruin(double p, int init_val=5){
    int T = 0;
    int M = 0;
    int curr_val = init_val;

    std::random_device rd;
    std::mt19937 engine(rd()); // Use Mersenne twister engine to generate random numbers
    std::uniform_real_distribution<> dist(0.0, 1.0); // Uniform distribution between 0 and 1

    while(curr_val>0){
        T++;
        if(dist(engine) < p){
            curr_val++;
            if(curr_val>M){
                M=curr_val;
            }
        }
        else {
            curr_val--;
        }
    }
    return std::make_pair(T,M);
}

void monte_carlo_method(double p, int n_times=pow(10,5)) {
    int* t = new int[n_times];
    int* m = new int[n_times];
    double mu_1, mu_2, mu_3;
    std::pair<int,int> tmp;

    for(int i = 0; i < n_times; i++){
        tmp = gamblers_ruin(p);
        t[i]=tmp.first;
        m[i]=tmp.second;
    }

    mu_1 = std::accumulate(t, t + n_times, 0.0)/n_times;
    mu_2 = std::accumulate(m, m + n_times, 0.0)/n_times;
    double count = std::count_if(m, m + n_times, [](int x) {
        return x >= 10;
    });
    mu_3 = count/n_times;

    double std_dev_T, std_dev_M;
    for(int i = 0; i < n_times; i++){
        std_dev_T+=pow(t[i]-mu_1,2);
        std_dev_M+=pow(m[i]-mu_2,2);
    }
    std_dev_T=sqrt(std_dev_T/n_times);
    std_dev_M=sqrt(std_dev_M/n_times);

    std::cout << "=============================\n";
    std::cout << "Probability: " << p << '\n';
    std::cout << "E[T]: " << mu_1 << " Standard Deviation of T: " << std_dev_T << '\n';
    std::cout << "E[M]: " << mu_2 << " Standard Deviation of M: " << std_dev_M << '\n';
    std::cout << "P[M>10]: " << mu_3 << '\n';
    std::cout << "=============================\n";
}

int main() {
    monte_carlo_method(0.4);
    monte_carlo_method(0.45);
    monte_carlo_method(0.48);
    return 0;
}