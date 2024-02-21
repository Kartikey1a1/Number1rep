from hub import light_matrix
import runloop

async def main():
    light_matrix.set_pixel(2,2,3)
    # first value is number of x-axis lights that will light up (from 0-4)
    # Second value is number of x-axis lights that will light up (from 0-4)
    #Third Value is the intensity of the lights 
    await light_matrix.write("Hi!")

runloop.run(main())
