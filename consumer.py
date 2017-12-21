import pika, os, time


def pdf_process_function(msg):
    print(' pdf processing')
    print(' recieved {}'.format(msg))

    time.sleep(5)
    print ('PDF processing finished')
    return


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1', retry_delay=3))
channel = connection.channel()
channel.queue_declare(queue='sampleQueue')


def callback(ch, method, properties, body):
    pdf_process_function(body)

channel.basic_consume(callback, queue='sampleQueue', no_ack=True)

channel.start_consuming()
connection.close()
