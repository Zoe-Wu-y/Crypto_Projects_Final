#include <stdint.h>
#include <string.h>

void sm3_compress(uint32_t state[8], const uint8_t block[64]) {
    // Basic SM3 compression function
}

void sm3_hash(const uint8_t *msg, size_t len, uint8_t out[32]) {
    // Padding + iteration over blocks
}
