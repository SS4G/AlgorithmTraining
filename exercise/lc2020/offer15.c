int hammingWeight(uint32_t n) {
    int cnt = 0;
    for (int i = 0; i < 32; i++) {
        if (n & (0x01 << i)) {
            cnt++;
        }
    }
    return cnt;
}