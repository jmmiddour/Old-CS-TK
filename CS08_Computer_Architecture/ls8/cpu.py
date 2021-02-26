"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.memory = [0] *256
        self.pc = 0
        self.flag = 0b00000000
        self.IR = {}
        self.reg = [0] * 8
        self.stopped = False
        self.SP = 244

        HLT = 0b00000001   # Halt - instruction handler - stops the program/computer
        LDI = 0b10000011   # Load Immediately - instruction -
        MUL = 0b10100010
        PRN = 0b01000111   # Print - Instruction -
        POP = 0b01000110   # Pop - removes value(s)
        PUSH = 0b01000101  # Push - adds value(s)
        RET = 0b00010001   # Return -
        CALL = 0b01010000  # Call -

        self.IR = {
                HLT =  self.HLT,   # Halt - Stops the program/computer
                LDI =  self.LDI,   # Load Immediately - instruction -
                MUL = self.MUL,  #
                PRN = self.PRN,  # Print - Instruction -
                POP = self.POP,  # Pop - Removes most recent value from the Stack
                PUSH = self.PUSH,  # Push - adds to Stack
                RET = self.RET,  # Return -
                CALL = self.CALL  # Call -
       }


    def HLT(self):  # Halt - stops the program/computer
        sys.exit()


    def LDI(self):  # Load Immediately -
        # Takes registry at the memory location of where we are currently at + 1,
        #   then moves it one over.
        self.reg[self.memory[self.pc + 1]] = self.reg[self.memory[self.pc + 2]]


    def PRN(self):  # Print - Holds the instructions for print function + 1
        # To avoid it from just printing print over and over, need to go to the
        #   next location in memory [self.pc + 1]
        print(self.reg[self.pc + 1])


    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:
        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def ram_read(self, MAR):  # MAR = Memory Address Register
        return self.reg(MAR)


    def ram_write(self, MDR):
        self.reg[MAR] = MDR


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def PC_move(self, operation):
        move = operation & 0b1000000
        move_num = (move >> 6) + 1
        return move_num


    def run(self):
        """Run the CPU."""
        operation = self.memory
        PC = self.pc

        while self.stopped == False:
            op = operation[PC]

            if op == 0b10000010:
                self.reg[operation[PC + 1]] = operation[PC + 2]
                PC += self.PC_move(op)

            elif op == 0b10100000:
                self.alu("ADD", self.memory[PC + 1], self.memory[PC + 2])
                PC += self.PC_move(op)

            elif op == 0b00001000:
                PC += self.PC_move(op)

            elif op == 0b10100010:
                self.alu("MULTI", self.memory[PC + 1], self.memory[PC + 2])
                PC += self.PC_move(op)

            elif op == 0b01000111:
                print(self.reg[operation[PC + 1]])
                PC += self.PC_move(op)

            elif op == 0b00000001:
                self.stopped = True
                self.HLT()
                PC += self.PC_move(op)

            elif op == 0b01000101:  # PUSH
                self.SP -= 1
                reg_loc = self.memory[PC + 1]
                self.memory[self.SP] = self.reg[reg_loc]
                self.reg[7] = self.SP
                PC += self.PC_move(op)

            elif op == 0b01000110:  # POP
                value = self.memory[self.reg[7]]
                reg_loc = self.memory[PC + 1]
                self.SP += 1
                self.reg[7] = self.SP
                self.reg[reg_loc] = value
                PC += self.PC_move(op)

            elif op == 0b01010000:  # CALL
                self.SP -= 1
                self.memory[self.SP] = PC + 2
                PC = self.reg[self.memory[PC + 1]]

            elif op == 0b00010001:  # RETURN
                PC = self.memory[self.SP]
                self.SP += 1

            elif op == 0b10100111:  # CMP
                self.FLG(self.memory[PC + 1], self.mempry[PC + 2])
                PC += self.PC_move(op)

            elif op == 0b01100110:  # DEC
                self.reg[PC + 1] -= 1
                PC += self.PC_move(op)

            elif op == 0b10100011:  # DIV
                self.alu("DIV", self.memory[PC + 1], self.memory[PC + 2])
                PC += self.PC_move(op)

            elif op == 0b01100101:  # INCR
                self.reg[self.memory[PC + 1]] += 1
                PC += self.PC_move(op)

            elif op == 0b01010101:  # JEQ
                if self.flag == 0b00000001:
                    PC = self.reg[self.memory[PC + 1]]
                else:
                    PC += self.PC_move(op)

            elif op == 0b01010110:  # JNE
                if self.flag != 0b00000001:
                    PC = self.reg[self.memory[PC + 1]]
                else:
                    PC += self.PC_move(op)

            elif op == 0b01010100:
                PC = self.reg[self.memory[PC + 1]]

            else:
                self.stopped = True
                print("Error: I am not a teapot")
                seld.HLT()
