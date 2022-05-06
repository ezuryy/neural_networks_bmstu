import numpy as np
import matplotlib.pyplot as plt
import random


class Point:

    def __init__(self, x, y, cluster=-1):
        self.x = x
        self.y = y
        self.cluster = cluster

    def euclidean_distance(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def chebyshev_distance(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.cluster == other.cluster

    def __ne__(self, other):
        return not self.__eq__(other)


class ClusteriserKMedians:

    def __init__(self):
        np.random.seed = 42
        self.points = []
        self.curr_medians = []
        self.cluster_number = -1
        self.output = ''

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def get_data_x_y_for_cluster(self, cl_num):
        x_cl = []
        y_cl = []
        for point in self.points:
            if point.cluster == cl_num:
                x_cl.append(point.x)
                y_cl.append(point.y)
        return x_cl, y_cl

    def get_median_for_cluster(self, cluster):
        x_cl = []
        y_cl = []
        for point in self.points:
            if point.cluster == cluster:
                x_cl.append(point.x)
                y_cl.append(point.y)
        return np.median(x_cl), np.median(y_cl)

    def update_euclidean_distance(self):
        for point in self.points:
            distances = [point.euclidean_distance(self.curr_medians[i])
                         for i in range(self.cluster_number)]
            point.cluster = np.argmin(distances)

    def update_chebyshev_distance(self):
        for point in self.points:
            distances = [point.chebyshev_distance(self.curr_medians[i])
                         for i in range(self.cluster_number)]
            point.cluster = np.argmin(distances)

    def show_current_state(self, start=False):
        markers = ['o', 'v', 'D', 's']
        fig, ax = plt.subplots(figsize=(4, 4))
        if start:
            print('start!')
            x_cl, y_cl = self.get_data_x_y_for_cluster(-1)
            ax.scatter(x_cl, y_cl, marker='o', label='points')
        else:
            for cluster in range(self.cluster_number):
                x_cl, y_cl = self.get_data_x_y_for_cluster(cluster)
                ax.scatter(x_cl, y_cl, marker=markers[cluster], label='cluster ' + str(cluster))
        median_x, median_y = get_data_x_y_of_median(self.curr_medians)
        ax.scatter(median_x, median_y, marker="d", label='cluster centers', c='red')
        ax.grid()
        ax.legend()

    def get_clusters(self, cl_num=2, dist='euclidean'):
        self.cluster_number = cl_num

        cluster_idx = list(range(len(self.points)))
        cluster_idx = random.sample(cluster_idx, k=self.cluster_number)

        for idx in cluster_idx:
            self.curr_medians.append(self.points[idx])

        iteration = 0
        self.show_current_state(True)
        plt.savefig('report' + str(iteration) + '.png')
        while True:
            prev_medians = self.curr_medians.copy()

            if dist == 'euclidean':
                self.update_euclidean_distance()
            else:
                self.update_chebyshev_distance()

            self.output += f'\nIteration #{iteration}\nCurrent state:\n'
            for p in self.points:
                self.output += f'{p.x}, {p.y}, {p.cluster}\n'

            for cluster in range(self.cluster_number):
                median_x, median_y = self.get_median_for_cluster(cluster)
                self.curr_medians[cluster] = Point(median_x, median_y)
                self.output += f'Median value for cluster {cluster}: {median_x}, {median_y}\n'

            if prev_medians == self.curr_medians:
                break
            iteration += 1
            self.show_current_state()
            plt.savefig('report' + str(iteration) + '.png')

        return iteration, self.output

    def clear_clusters(self):
        for point in self.points:
            point.cluster = -1
        self.curr_medians = []
        self.cluster_number = -1
        self.output = ''


def get_data_x_y_of_median(median):
    x_cl = []
    y_cl = []
    for point in median:
        x_cl.append(point.x)
        y_cl.append(point.y)
    return x_cl, y_cl


if __name__ == '__main__':
    model = ClusteriserKMedians()
    model.add_point(143, 213)
    model.add_point(180, 220)
    model.add_point(183, 249)
    model.add_point(271, 253)
    model.add_point(226, 253)
    model.add_point(315, 275)
    model.add_point(266, 297)
    model.get_clusters(2, 'chebyshev')
