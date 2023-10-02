#include <random>
#include <utility>
#include <random>
#include <cmath>
#include <iostream>
#include <numeric>
#include <algorithm>
#include <unordered_map>

std::pair<int, int> no_of_coupons(int n_types) {
    std::vector<int> coupon_count(n_types, 0); // Initialize with zeros

    std::random_device rd;
    std::mt19937 engine(rd());
    std::uniform_int_distribution<> dist(0, n_types - 1); // Uniform distribution for n_types

    int unique_vals = n_types;
    while(unique_vals > 0) {
        int coupon_tmp = dist(engine);
        if(coupon_count[coupon_tmp]++ == 0) {
            unique_vals--;
        }
    }

    int t = std::accumulate(coupon_count.begin(), coupon_count.end(), 0);
    int max_collected = *std::max_element(coupon_count.begin(), coupon_count.end());

    return {t, max_collected}; // Using list initialization for pair
}

void monte_carlo_method(int n, long int n_times=pow(10,5)) {
    int* t = new int[n_times];
    int* m = new int[n_times];
    double mu1,mu2;
    std::pair<int,int> tmp;

    for(int i = 0; i < n_times; i++){
        tmp = no_of_coupons(n);
        t[i] = tmp.first;
        m[i] = tmp.second;
    }

    mu1 = std::accumulate(t, t + n_times, 0.0)/n_times;
    mu2 = std::accumulate(m, m + n_times, 0.0)/n_times;

    double std_dev_M,std_dev_T;
    for(int i = 0; i < n_times; i++){
        std_dev_T+=pow(t[i]-mu1,2);
        std_dev_M+=pow(m[i]-mu2,2);
    }
    std_dev_T=sqrt(std_dev_T/n_times);
    std_dev_M=sqrt(std_dev_M/n_times);

    std::cout << "=============================\n";
    std::cout << "Number of types of coupons: " << n << '\n';
    std::cout << "E[T]: " << mu1 << " Standard Deviation of T: " << std_dev_T << '\n';
    std::cout << "E[X]: " << mu2 << " Standard Deviation of M: " << std_dev_M << '\n';
    std::cout << "=============================\n";
}

int main() {
    monte_carlo_method(10);
    monte_carlo_method(20);
    return 0;
}