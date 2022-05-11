import copy


class RR:
    def _init_(self):
        self.ready_queue = []
        self.processes = []
        self.quantum = 2

        print("Round Robin Scheduling with Quantum 2ns")
        self.n = int(input("Enter the number of processes: "))
        for i in range(self.n):
            arrival = int(input(f"Enter the arrival time for process {i+1}: "))
            burst = int(input(f"Enter the burst time for process {i+1}: "))
            self.processes.append([i, arrival, burst, False])

    def sort(self, index):
        for i in range(len(self.processes)):
            for j in range(0, len(self.processes) - i - 1):
                if self.processes[j][index] > self.processes[j+1][index]:
                    temp = self.processes[j]
                    self.processes[j] = self.processes[j+1]
                    self.processes[j+1] = temp

    def roundRobinScheduling(self):
        self.time_elapsed = self.processes[0][1]
        self.processes_copy = copy.deepcopy(self.processes)
        self.display_data = []
        self.order = []
        while True:
            all_done = True
            for process in self.processes_copy:
                if process[2] > 0:
                    all_done = False
            if all_done:
                break
            self.setProcessArrival()
            current_process = self.ready_queue.pop(0)
            for i in range(len(self.processes)):
                if self.processes[i][0] == current_process[0]:
                    index = i
            if self.processes_copy[index][2] < self.quantum:
                self.time_elapsed += self.processes_copy[index][2]
                self.processes_copy[index][2] = 0
            else:
                self.processes_copy[index][2] -= self.quantum
                self.time_elapsed += self.quantum
            if self.processes_copy[index][2] > 0:
                self.setProcessArrival()
                self.order.append(f"P[{index+1}]")
                self.ready_queue.append(self.processes_copy[index])
            else:
                self.display_data.append([index+1, self.processes[index][1], self.processes[index][2], self.time_elapsed -
                                         self.processes[index][2] - current_process[1], self.time_elapsed - current_process[1], self.time_elapsed])

    def setProcessArrival(self):
        for process in self.processes_copy:
            if process[1] <= self.time_elapsed and process[2] > 0 and process[3] == False:
                self.order.append(f"P[{process[0]+1}]")
                process[3] = True
                self.ready_queue.append(process)

    def displayTable(self):
        # Sort display data
        for i in range(len(self.display_data)):
            for j in range(0, len(self.display_data) - i - 1):
                if self.display_data[j][0] > self.display_data[j+1][0]:
                    temp = self.display_data[j]
                    self.display_data[j] = self.display_data[j+1]
                    self.display_data[j+1] = temp
                    print("Sorting")
        print("Processes\tBurst Time\tArrival Time\tWaiting Time\tTurn-Around Time\tCompletion Time")
        for data in self.display_data:
            print(
                f"P[{data[0]}]\t\t{data[2]}\t\t{data[1]}\t\t{data[3]}\t\t{data[4]}\t\t\t{data[5]}")


def main():
    rr = RR()
    rr.sort(1)
    rr.roundRobinScheduling()
    rr.displayTable()


if _name_ == "_main_":
    main()
