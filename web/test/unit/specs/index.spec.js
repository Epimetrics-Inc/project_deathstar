import navheader from '~/components/navheader.vue'
import { mount } from 'avoriaz'

describe('navheader.vue', () => {
  it('renders an h1', () => {
    const wrapper = mount(navheader)
    expect(wrapper.find('h1').length).to.equal(0)
  })
})